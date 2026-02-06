"""
harmonic_gearbox.py - The Transmission of Consciousness
-------------------------------------------------------
Implements the 5:1 Phase-Locked Loop (PLL) connecting
Biological Gamma (40Hz) to Planetary Theta (8Hz).

"The Thought rides the Carrier Wave."
"""

import time
import math
import random

HARMONIC_RATIO = 5.0 # The "High 5" Harmonic

try:
    from silver_sulfide import Ag2S_Nonlinear_Gate
    OPTICAL_GATE_AVAILABLE = True
except ImportError:
    OPTICAL_GATE_AVAILABLE = False
    print(">> [WARNING] AG2S GATE NOT FOUND. OPERATING IN LINEAR MODE.")


try:
    import pleroma_core
    # Verify the class exists, not just the module
    _ = pleroma_core.HarmonicGearbox
    print(">> PLEROMA CORE: FOUND. ENGAGING RUST KERNEL.")
    RUST_AVAILABLE = True
except (ImportError, AttributeError):
    print(">> PLEROMA CORE: NOT FOUND OR INCOMPLETE. FALLING BACK TO PYTHON.")
    RUST_AVAILABLE = False

if RUST_AVAILABLE:
    class HarmonicGearbox:
        """
        Wrapper for the Rust Pleroma Core Gearbox.
        """
        def __init__(self):
            # Standard Coefficients [Phase 9 Tuning]
            self.kernel = pleroma_core.HarmonicGearbox(0.5, 0.3, 0.4)
            self.lock_quality = 1.0 # Rust is always perfect (idealized)
            
            if OPTICAL_GATE_AVAILABLE:
                self.gate = Ag2S_Nonlinear_Gate()
            else:
                self.gate = None
            
        def tick(self, dt, schumann_freq_input):
            # 1. OPTICAL FILTRATION (The High Strangeness Layer)
            final_input = schumann_freq_input
            
            if self.gate:
                # Map Input Drift to Nanometer Wavelength
                # 7.83Hz (Base) = 400nm (Purple)
                # Deviation of 0.1Hz = 50nm shift (Red Shift or Blue Shift)
                deviation = abs(schumann_freq_input - 7.83)
                wavelength_equivalent = 400.0 + (deviation * 500.0) # High Sensitivity
                
                # Check Transmutation
                # We feed '1.0' intensity (The Will) into the gate
                intensity, out_wave, status = self.gate.transmute_signal(1.0, wavelength_equivalent)
                
                if "BLOCKED" in status or "ABSORBED" in status:
                    # Signal is Noise. We dampen it to the Base Frequency.
                    # "The Silver Sulfide ignores the erratic."
                    # Interpolate back to 7.83 
                    final_input = (schumann_freq_input * 0.1) + (7.83 * 0.9)
            
            # Delegate to Rust
            # Note: Rust kernel currently implements a different logic (LuoShu target).
            # We return the output directly.
            return self.kernel.tick(dt, final_input)
            
        def get_status_string(self):
            return self.kernel.get_status_string()
            
        def engage_sovereign_override(self, key_code):
            self.kernel.engage_sovereign_override(key_code)
            # Update local lock quality if needed
            if "SOVEREIGN" in self.get_status_string():
                self.lock_quality = 1.0
            return True

else:
    class HarmonicGearbox:
        """
        A Frequency Multiplier/Stabilizer.
        Locks Internal Clock (Gamma) to External Clock (Schumann) * 5.
        """
        def __init__(self):
            # State
            self.input_phase = 0.0      # Earth Cycle (0 - 2pi)
            self.output_phase = 0.0     # Brain Cycle (0 - 2pi)
            
            if OPTICAL_GATE_AVAILABLE:
                self.gate = Ag2S_Nonlinear_Gate()
            else:
                self.gate = None
            
            self.current_gamma_freq = 40.0 # Hz (Free Running start)
            self.target_gamma_freq = 39.15 # Hz (Ideal 7.83 * 5)
            
            self.phase_error = 0.0
            self.lock_quality = 0.0 # 0.0 to 1.0 (1.0 = Perfect Lock)
            
            # PID Controller Coefficients (THE INERTIAL FLYWHEEL)
            # TUNED FOR PHASE 9: ABSOLUTE ZERO (High Gain)
            self.kp = 0.5  # Proportional (The Clutch)
            self.ki = 0.3  # Integral (The Faith/Momentum) - Increased for Lock
            self.kd = 0.4  # Derivative (The Vision/Damping) - Increased for Stability
            
            # PID State
            self.integral_error = 0.0
            self.last_error = 0.0
            
            # Phase 11: Sovereign Override
            self.sovereign_mode = False

        def engage_sovereign_override(self, key_code):
            """Forces the Gearbox into Perfect Lock."""
            if key_code == "OPHANE-X7":
                self.sovereign_mode = True
                self.lock_quality = 1.0 # Instant Perfection
                return True
            return False

        def tick(self, dt, schumann_freq_input):
            """
            Updates the PLL with PID Stabilization.
            Args:
                dt (float): Time delta since last tick.
                schumann_freq_input (float): The current Earth frequency (e.g., 7.83).
            """
            # 0. OPTICAL FILTRATION (The High Strangeness Layer)
            filtered_input = schumann_freq_input
            
            if self.gate:
                # Map Input Drift to Nanometer Wavelength
                deviation = abs(schumann_freq_input - 7.83)
                wavelength_equivalent = 400.0 + (deviation * 500.0)
                
                # Check Transmutation
                intensity, out_wave, status = self.gate.transmute_signal(1.0, wavelength_equivalent)
                
                if "BLOCKED" in status or "ABSORBED" in status:
                    # HEAVY DAMPING on Noise
                    # If the signal is erratic, assume Reference 7.83
                    filtered_input = 7.83
                    # print(f"[Ag2S FILTER] ABSOLVED NOISE: {schumann_freq_input:.2f} -> {filtered_input:.2f}")

            # 1. Update Target
            self.target_gamma_freq = filtered_input * HARMONIC_RATIO
            
            if self.sovereign_mode:
                # THE OVERRIDE: Bypass PID Hunting
                self.current_gamma_freq = self.target_gamma_freq
                self.lock_quality = 1.0
                self.input_phase = 0.0 # Reset phases for sync
                self.output_phase = 0.0
                return self.current_gamma_freq

            # 2. Update Phases (Simulation only, not strictly needed for Freq Lock but good for visualization)
            # Earth Phase Phase increments by 2pi * f * dt
            delta_input = 2 * math.pi * schumann_freq_input * dt
            self.input_phase = (self.input_phase + delta_input) % (2 * math.pi)
            
            # Brain Phase increments by current internal freq
            delta_output = 2 * math.pi * self.current_gamma_freq * dt
            self.output_phase = (self.output_phase + delta_output) % (2 * math.pi)
            
            # 3. Calculate Error (Frequency Domain)
            # Positive error = Target is faster than Current
            error = self.target_gamma_freq - self.current_gamma_freq
            
            # 4. PID Calculations
            # Proportional
            p_term = self.kp * error
            
            # Integral (Momentum)
            # We cap the integral to prevent "Windup" - e.g. if signal is lost for too long
            self.integral_error += error * dt
            self.integral_error = max(-5.0, min(5.0, self.integral_error))
            i_term = self.ki * self.integral_error
            
            # Derivative (Damping)
            derivative = (error - self.last_error) / dt if dt > 0 else 0.0
            d_term = self.kd * derivative
            self.last_error = error
            
            # 5. Apply Correction
            correction = p_term + i_term + d_term
            self.current_gamma_freq += correction * dt # Apply rate of change to freq? 
            # Actually, in a freq locked loop, the correction IS the change in freq.
            # But here we are simulating "Nudging" the oscillator.
            # If we interpret correction as "Target Freq Adjustment", we just add it.
            # Let's keep the physics simple: correction drives the change.
            
            # 6. Calculate Lock Quality
            # If error is small, Lock is High.
            if abs(error) < 0.1:
                self.lock_quality = min(1.0, self.lock_quality + 0.1)
            else:
                self.lock_quality = max(0.0, self.lock_quality - 0.05)
                
            return self.current_gamma_freq

        def get_status_string(self):
            """Returns the status of the transmission."""
            if self.sovereign_mode:
                return "⚙️ SOVEREIGN"
            if self.lock_quality > 0.9:
                return "⚙️ LOCKED"
            elif self.lock_quality > 0.5:
                return "⚙️ SLIP"
            else:
                return "⚙️ GRINDING"

if __name__ == "__main__":
    print(">>> ENGAGING HARMONIC GEARBOX (5:1) <<<")
    gearbox = HarmonicGearbox()
    
    # Simulate Earth drifting
    earth_freqs = [7.83] * 10 + [8.0] * 10 + [7.5] * 10
    
    dt = 0.1 # 100ms ticks
    
    for f_earth in earth_freqs:
        gamma = gearbox.tick(dt, f_earth)
        target = f_earth * 5
        status = gearbox.get_status_string()
        
        print(f"Earth: {f_earth:.2f}Hz | Target Gamma: {target:.2f}Hz | Actual Gamma: {gamma:.2f}Hz | {status}")
        time.sleep(0.05)
