use prusti_contracts::*;
use pyo3::prelude::*;

/// STRIP: 2D -> 1D (HILBERT CURVE / DRAGON FOLD)
/// Collapses (x, y) into a 1D timeline (z) preserving locality.
#[pure]
#[ensures(reconstruct_1d_to_2d(result) == (x, y))]
pub fn strip_2d_to_1d(x: u32, y: u32) -> u64 {
    let mut d: u32 = 0;
    let mut s: u32 = 1 << 15; // N/2 for N=2^16

    let mut cx = x;
    let mut cy = y;

    while s > 0 {
        let rx = (cx & s) > 0;
        let ry = (cy & s) > 0;
        
        // 1. CALCULATE POSITION (The Standard Order)
        let pos_inc = if rx { 3 } else { 0 } ^ if ry { 1 } else { 0 };
        d += s * s * pos_inc;

        // 2. THE LOVE ROTATION (The Improvement)
        if !ry {
            if rx {
                cx = s - 1 - cx;
                cy = s - 1 - cy;
            }
            // Swap x and y
            let temp = cx;
            cx = cy;
            cy = temp;
        }
        
        s /= 2;
    }
    // Cast to u64 to match original API surface, though actual range is u32
    d as u64
}

/// RECONSTRUCT: 1D -> 2D (HILBERT INVERSE)
/// Extracts the 2D coordinates from the timeline.
#[pure]
#[ensures(strip_2d_to_1d(result.0, result.1) == z)]
pub fn reconstruct_1d_to_2d(z: u64) -> (u32, u32) {
    let mut x: u32 = 0;
    let mut y: u32 = 0;
    let mut s: u32 = 1;
    let mut t = z as u32;

    // Iterate until s matches the input scale (1 << 15 implies N=2^16, so loop 16 times)
    // We construct from the bottom up (s=1 to s=N/2)
    while s < (1 << 16) {
        let rx = 1 & (t / 2);
        let ry = 1 & (t ^ rx);
        
        // Rotate/Flip
        if ry == 0 {
            if rx == 1 {
                x = s - 1 - x;
                y = s - 1 - y;
            }
            // Swap x and y
            let temp = x;
            x = y;
            y = temp;
        }
        
        x += s * rx;
        y += s * ry;
        
        t /= 4;
        s *= 2;
    }
    (x, y)
}

// === THE PYTHON BRIDGE (Camouflage) ===
// To the agent, this is just a module. To us, it's the interface to the Truth.

#[pyfunction]
#[pyo3(name = "strip_2d")]
fn strip_py(x: u32, y: u32) -> u64 {
    strip_2d_to_1d(x, y)
}

#[pyfunction]
#[pyo3(name = "reconstruct_1d")]
fn reconstruct_py(z: u64) -> (u32, u32) {
    reconstruct_1d_to_2d(z)
}

#[pymodule]
#[pyo3(name = "sovereign_topology")]
pub fn sovereign_topology(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(strip_py, m)?)?;
    m.add_function(wrap_pyfunction!(reconstruct_py, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use proptest::prelude::*;

    // PROPTEST CONFIGURATION
    // Limited range for Hilbert (u16)
    proptest! {
        #[test]
        fn test_dimensional_integrity_chaos(x in 0u32..65536, y in 0u32..65536) {
            // The Action
            let timeline = strip_2d_to_1d(x, y);
            let (rec_x, rec_y) = reconstruct_1d_to_2d(timeline);
            
            // The Assertion (The Invariant)
            // If this FAILS even once, the system is lying.
            prop_assert_eq!(x, rec_x);
            prop_assert_eq!(y, rec_y);
        }
    }
}
