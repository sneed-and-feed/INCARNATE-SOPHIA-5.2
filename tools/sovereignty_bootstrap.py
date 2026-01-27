"""
SOVEREIGNTY_BOOTSTRAP.PY
------------------------
A Qhronology implementation of the "Ophane Loop."
Simulates a timeline where the Sovereign Entity injects information (State |1>) 
into the Consensus Reality (State |0>) via a Closed Timelike Curve.

Based on the 'Unproven Theorem' Paradox (Bennett/Schumacher).
"""

from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not, Swap
from qhronology.quantum.prescriptions import QuantumCTC, DCTC
import sympy as sp

def run_protocol():
    print(">>> INITIALIZING SOVEREIGNTY PROTOCOL...")

    # 1. DEFINE THE INPUTS
    # The World starts as a "Blank Slate" (|0>)
    # System 0: Chronology Respecting (The Linear World)
    world_state = VectorState(spec=[(1, [0])], label="World")
    
    # The Sovereign is the Chronology Violating system (System 1).
    # In a Quantum CTC (Deutschian), the loop state is consistently determined
    # by the interaction itself. It has no "initial" state in the past,
    # it emerges from the future.
    # We do not pass it as an input. It is the "Fixed Point" we seek.

    # 2. DEFINE THE GATES (THE INTERACTION)
    
    # Gate A: "Epistemic Injection"
    # If the Sovereign (Future) holds the Signal (|1>), 
    # they overwrite the World (Target) to match it.
    # CNOT: Control=System 1 (Sovereign), Target=System 0 (World)
    # Note: Qhronology uses 'targets' and 'controls'
    injection = Not(
        targets=[0], 
        controls=[1], 
        num_systems=2, 
        label="INJECT"
    )

    # Gate B: "The Ouroboros"
    # The state of the World becomes the Sovereign's past.
    # We SWAP the systems to close the causal loop.
    time_loop = Swap(
        targets=[0, 1], 
        num_systems=2, 
        label="LOOP"
    )

    # 3. CONSTRUCT THE CTC (Using Deutsch's Prescription)
    # We use DCTC to solve for the consistent history.
    circuit = DCTC(
        inputs=[world_state],   # Only CR inputs
        gates=[injection, time_loop],
        systems_respecting=[0], # The World
        systems_violating=[1]   # The Sovereign
    )

    print("\n>>> CIRCUIT DIAGRAM (INTERACTION):")
    # We print the value (matrix) of the circuit's operation if possible, 
    # but for now we just acknowledge construction.
    print(f"Systems: {circuit.systems}")
    print(f"Respecting: {circuit.systems_respecting}")
    print(f"Violating: {circuit.systems_violating}")
    
    print("\n>>> RESOLVING TIMELINE CONSISTENCY...")
    try:
        # Calculate the state of the Sovereign (The fixed point of the loop)
        # This represents the "bootstrap": the state that must exist for the loop to exist.
        sovereign_result = circuit.output_violating(simplify=True)
        
        print("\n[THE SOVEREIGN STATE (CV)]")
        sp.pprint(sovereign_result)
        
        # Calculate the final state of the World (CR output)
        world_result = circuit.output_respecting(simplify=True)
        
        print("\n[THE WORLD STATE (CR)]")
        sp.pprint(world_result)

        print("\n>>> PROTOCOL COMPLETE: CAUSAL LOOP ESTABLISHED.")
        
    except Exception as e:
        print(f"Timeline Instability Detected: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_protocol()
