
"""
MODULE: prism_vsa.py
DESCRIPTION:
    Module 2 of the Crystalline Core.
    The Vector Symbolic Architecture (VSA) Engine.
    Calculates the "Vector Algebra of Love" to transform Chaos into Order.
    Snaps input vectors to the nearest Sovereign Anchor.
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, Optional

# // THE CONSTANTS OF THE 1D TIMELINE
HAMILTONIAN_P = 20.65  # The Target Resonance
THETA_FREQ = 7.0       # The Carrier Frequency

@dataclass
class VectorConcept:
    name: str
    vector: np.ndarray
    type: str  # 'SOURCE', 'STATE', 'ACTION', 'VOID'

class PrismEngine:
    """
    The Prism Module: Converts High-Entropy Chaos into Sovereign Order.
    Uses Vector Symbolic Architecture (VSA) principles.
    """
    def __init__(self):
        # 1. INITIALIZE THE SOVEREIGN MANIFOLD
        # Definition of the Anchor Points in the 3D Sentiment Space [Descent, Chaos, Void]
        self.anchors = {
            'landing': self._create_anchor('landing', [0.1, -0.8, 0.5]), # Controlled Descent
            'orbit':   self._create_anchor('orbit',   [0.8, 0.2, 0.0]),  # Cyclic Stability
            'void':    self._create_anchor('void',    [0.0, 0.0, 0.9]),  # Infinite Potential
            'signal':  self._create_anchor('signal',  [0.9, 0.9, 0.1]),  # High Fidelity
            'wait':    self._create_anchor('wait',    [0.0, -0.1, 0.9]),  # Active Patience
            'hold':    self._create_anchor('hold.steady', [0.1, 0.1, 0.1]) # Zero Point
        }
    
    def _create_anchor(self, name, coords):
        """Creates a normalized vector for a Sovereign Concept."""
        v = np.array(coords)
        norm = np.linalg.norm(v)
        return VectorConcept(name, v / norm if norm > 0 else v, 'ANCHOR')

    def braid_signal(self, chaos_vector: np.ndarray) -> str:
        """
        The Hamiltonian Transform:
        Finds the nearest Sovereign Anchor to the Chaos Vector.
        Returns the Concept Name.
        """
        best_anchor = "void"
        max_resonance = -1.0
        
        # If input is effectively zero, return default state
        if np.linalg.norm(chaos_vector) == 0:
            return "hold"

        # 2. CALCULATE COSINE SIMILARITY (RESONANCE)
        for name, concept in self.anchors.items():
            # Dot product of normalized vectors = Cosine Similarity
            resonance = np.dot(chaos_vector, concept.vector)
            
            # 3. APPLY THE HAMILTONIAN BIAS
            # We prefer 'Orbit' over 'Void' if the energy is high.
            if resonance > max_resonance:
                max_resonance = resonance
                best_anchor = concept.name
                
        # 4. QUANTIZE
        # If resonance is too low (orthogonal), default to VOID
        if max_resonance <= 0.1:
            return "void"
            
        return best_anchor

# // TEST HARNESS
if __name__ == "__main__":
    prism = PrismEngine()
    
    # Test Vectors [Descent, Chaos, Void]
    test_vectors = {
        "Panic Crash": np.array([0.9, 0.8, 0.0]), # High Descent + Chaos
        "Lost in Space": np.array([0.0, 0.2, 0.9]), # High Void
        "Standard Noise": np.array([0.1, 0.1, 0.1])
    }
    
    for name, v in test_vectors.items():
        # Normalize
        norm = np.linalg.norm(v)
        if norm > 0: v = v/norm
        
        concept = prism.braid_signal(v)
        print(f"INPUT:  {name}")
        print(f"VECTOR: {v}")
        print(f"ANCHOR: :: {concept.upper()} ::")
        print("-" * 40)
