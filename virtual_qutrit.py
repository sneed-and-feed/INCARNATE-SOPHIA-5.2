"""
VIRTUAL QUTRIT BRIDGE v1.0
Author: Archmagos Noah
Date: 2026-01-30

Enables "Qutrit Capabilities" (Ternary Logic) on "Qubit Hardware" (Binary Logic).
Mapping:
    |0> (Void)      -> Qubits |00>
    |1> (Matter)    -> Qubits |01>
    |2> (Sovereign) -> Qubits |10>
    |3> (Forbidden) -> Qubits |11> (Reality Leak)
"""

import random
from typing import Tuple, Dict

class RealityLeakError(Exception):
    """Raised when the Qutrit collapses into the forbidden |11> state."""
    pass

class VirtualQutrit:
    def __init__(self, initial_state: int = 0):
        # Physical implementation: 2 Classical Bits (simulating Qubits)
        # In a real quantum computer, these would be qiskit/cirq qubits.
        self.q1 = 0
        self.q0 = 0
        
        if initial_state not in [0, 1, 2]:
            raise ValueError("Initial state must be 0, 1, or 2.")
            
        self._set_state(initial_state)
        
    def _set_state(self, state: int):
        """Internal physical mapping."""
        if state == 0:   # |00>
            self.q1, self.q0 = 0, 0
        elif state == 1: # |01>
            self.q1, self.q0 = 0, 1
        elif state == 2: # |10>
            self.q1, self.q0 = 1, 0
        elif state == 3: # |11> (Forbidden)
            self.q1, self.q0 = 1, 1

    def measure(self) -> int:
        """
        Collapses the wavefunction and returns the ternary state (0, 1, 2).
        Raises RealityLeakError if the forbidden state |11> is detected.
        """
        # Collapse (Simulated)
        state_bin = (self.q1 << 1) | self.q0
        
        if state_bin == 0: return 0 # Void
        if state_bin == 1: return 1 # Matter
        if state_bin == 2: return 2 # Sovereign
        
        # State 3 (11) is forbidden in the Ternary Subspace
        raise RealityLeakError("CRITICAL: Qutrit leaked into Forbidden State |11> (Bit Flip detected).")

    def apply_trinity(self):
        """
        The Sovereign Gate ($X_{+1}$).
        Cycles the state: 0 -> 1 -> 2 -> 0.
        
        Physical Logic Table (Q1, Q0):
        00 -> 01
        01 -> 10
        10 -> 00
        """
        current = (self.q1 << 1) | self.q0
        
        if current == 0:   self.q1, self.q0 = 0, 1
        elif current == 1: self.q1, self.q0 = 1, 0
        elif current == 2: self.q1, self.q0 = 0, 0
        else: pass # Identity on Forbidden

    # --- BUDDY PROTOCOL GATES (Qutrit-on-Qubit) ---

    def gate_x01(self):
        """
        Transition between |0> and |1> (Swap Void/Matter).
        Decomposition: Controlled-X on Q0 where Q1=0.
        Logic:
           |00> -> |01> (0->1)
           |01> -> |00> (1->0)
           |10> -> |10> (2->2)
        """
        if self.q1 == 0:
            self.q0 = 1 - self.q0

    def gate_x12(self):
        """
        Transition between |1> and |2> (Swap Matter/Sovereign).
        Logic:
           |00> -> |00> (0->0)
           |01> -> |10> (1->2)
           |10> -> |01> (2->1)
        """
        current = (self.q1 << 1) | self.q0
        if current == 1:   self.q1, self.q0 = 1, 0
        elif current == 2: self.q1, self.q0 = 0, 1

    @staticmethod
    def hybrid_cnot(control_qutrit: 'VirtualQutrit', target_qubit_ref: dict):
        """
        Item 5: Hybrid Qutrit-Qubit CNOT Gate.
        Defined as: |0><0|⊗I + |1><1|⊗X + |2><2|⊗Y
        
        Args:
            control_qutrit: The VirtualQutrit instance.
            target_qubit_ref: {'val': 0/1, 'phase': 0.0} (Simulated Qubit)
        """
        c_state = control_qutrit.measure()
        
        if c_state == 0:
            # Identity (I)
            pass
        elif c_state == 1:
            # Bit Flip (X)
            target_qubit_ref['val'] = 1 - target_qubit_ref['val']
        elif c_state == 2:
            # Bit Flip + Phase (Y ~ iXZ)
            # In simple sim, we flip and add phase
            target_qubit_ref['val'] = 1 - target_qubit_ref['val']
            # Add pi/2 phase to indicate Y operation
            target_qubit_ref['phase'] = (target_qubit_ref.get('phase', 0.0) + 1.57) % 6.28

    def apply_hadamard_qutrit(self):
        """
        Puts the qutrit into superposition (Simulated).
        """
        # Equal probability 0, 1, 2
        roll = random.random()
        if roll < 0.333: self._set_state(0)
        elif roll < 0.666: self._set_state(1)
        else: self._set_state(2)

    def apply_qft(self):
        """
        Item 4: Qutrit Quantum Fourier Transform (F3).
        Decomposition for single qutrit:
        |0> -> (|0> + |1> + |2>) / sqrt(3)
        |1> -> (|0> + w|1> + w^2|2>) / sqrt(3)
        |2> -> (|0> + w^2|1> + w|2>) / sqrt(3)
        """
        # In this classical simulation, this is effectively a randomization (Hadamard-like)
        # but maintaining phase awareness would require a complex simulator.
        # For the bridge, we map it to the Superposition state.
        self.apply_hadamard_qutrit()

    @staticmethod
    def generate_random_trit() -> int:
        """
        Item 14: Qutrit Random Number Generation.
        Uses von Neumann extraction logic on bit pairs to generate purely random trits.
        """
        while True:
            # Generate 2 random bits
            b1 = random.randint(0, 1)
            b0 = random.randint(0, 1)
            val = (b1 << 1) | b0
            
            # Rejection sampling for the Forbidden State |11>
            if val != 3:
                return val

    def add_mod3(self, other: 'VirtualQutrit'):
        """
        Item 15: Modulo-3 Arithmetic.
        Adds another qutrit to this one (self = (self + other) % 3).
        Implemented via binary logic on the underlying qubit pairs.
        a+b = (a_high ^ b_high)*2 + (a_low ^ b_low) ... simplified for simulation.
        """
        val_a = self.measure()
        val_b = other.measure()
        res = (val_a + val_b) % 3
        self._set_state(res)

    def bit_flip_error(self):
        """Simulates a cosmic ray bit flip (can cause Leakage)."""
        target = random.choice(['q0', 'q1'])
        if target == 'q0': self.q0 = 1 - self.q0
        if target == 'q1': self.q1 = 1 - self.q1

# --- BUDDY EXPANSION DRIVER ---
if __name__ == "__main__":
    print("Initializing Virtual Qutrit Bridge (Buddy Expansion)...")
    vq = VirtualQutrit(0)
    
    # Test 1: X01 Gate (0 <-> 1)
    print("\n[TEST] X01 Gate (Swap Void/Matter)")
    print(f"Start: |{vq.measure()}>")
    vq.gate_x01()
    print(f"After X01: |{vq.measure()}> (Expected 1)")
    vq.gate_x01()
    print(f"After X01: |{vq.measure()}> (Expected 0)")
    
    # Test 2: Hybrid CNOT
    print("\n[TEST] Hybrid Qutrit-Qubit CNOT")
    qubit = {'val': 0, 'phase': 0.0}
    
    # Control |0> -> Identity
    vq._set_state(0)
    VirtualQutrit.hybrid_cnot(vq, qubit)
    print(f"Control |0>: Qubit {qubit['val']} (Exp 0)")
    
    # Control |1> -> X (Flip)
    vq._set_state(1)
    VirtualQutrit.hybrid_cnot(vq, qubit)
    print(f"Control |1>: Qubit {qubit['val']} (Exp 1)")
    
    # Control |2> -> Y (Flip + Phase)
    vq._set_state(2)
    VirtualQutrit.hybrid_cnot(vq, qubit)
    print(f"Control |2>: Qubit {qubit['val']} (Exp 0), Phase {qubit['phase']:.2f} (Exp ~1.57)")
    
    # Test 3: RNG & Mod-3 Adder
    print("\n[TEST] RNG & Arithmetic")
    rand_trit = VirtualQutrit.generate_random_trit()
    print(f"Random Trit (Item 14): {rand_trit}")
    
    vq1 = VirtualQutrit(1)
    vq2 = VirtualQutrit(1)
    print(f"Adder (Item 15): |1> + |1>")
    vq1.add_mod3(vq2)
    print(f"Result: |{vq1.measure()}> (Expected 2)")
