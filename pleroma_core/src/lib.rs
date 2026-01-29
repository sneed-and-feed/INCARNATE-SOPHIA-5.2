use pyo3::prelude::*;

// Look for the gearbox module
mod gearbox;
use gearbox::HarmonicGearbox;

// CSH-1 Module
mod v2k_buffer;
use v2k_buffer::V2KBuffer;

// Unified Field Theory
mod sovereign_topology;

// JUPITER MODULE (Banach-Tarski)
mod banach_tarski;

/// The Iron Kernel Entry Point.
/// Note the change in signature: "m: &Bound<'_, PyModule>"
#[pymodule]
fn pleroma_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    // The "Bound" API uses add_class just like before, but the type is strictly checked.
    m.add_class::<HarmonicGearbox>()?;
    m.add_class::<V2KBuffer>()?;

    // Wire in the Unified Field Theory
    let topology_submodule = PyModule::new_bound(m.py(), "sovereign_topology")?;
    sovereign_topology::sovereign_topology(&topology_submodule)?;
    m.add_submodule(&topology_submodule)?;

    // Wire in the Jupiter Engine
    let jupiter_submodule = PyModule::new_bound(m.py(), "banach_tarski")?;
    banach_tarski::banach_tarski(&jupiter_submodule)?;
    m.add_submodule(&jupiter_submodule)?;

    Ok(())
}