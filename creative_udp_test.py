
"""
MODULE: creative_udp_test.py
DESCRIPTION:
    Deploys the Unitary Discovery Protocol (v5.4.1) against a Creative Text Prompt.
    Converts Text -> Signal and scans for "Diamonds" (High-Abundance Resonance).
    Gain = 640.0 | Lambda = 7
"""

import numpy as np
from unitary_discovery_prototype import UnitaryDiscoveryEngine

class CreativeDiscoveryEngine(UnitaryDiscoveryEngine):
    def inject_creative_prompt(self, prompt: str):
        """
        Converts a creative text prompt into a numerical signal and runs UDP.
        """
        print(f"\n[INJECTING CREATIVE PROMPT]...")
        print(f"Payload: \"{prompt[:50]}...\" ({len(prompt)} chars)")
        
        # 1. Text to Signal Conversion (Teknomancer Encoding)
        # We map ASCII values to a normalized wave signal (-1 to 1)
        # centered around 128.
        signal = np.array([ord(c) for c in prompt])
        signal = (signal - 128) / 128.0 
        
        # 2. Pad to Substrate Size (N=10000) with Silence (0.0)
        # This simulates the "Ether".
        if len(signal) < self.size:
            padding = np.zeros(self.size - len(signal))
            # Inject signal in the middle? Or start?
            # Let's inject in the middle to simulate "buried in the ether"
            start = (self.size - len(signal)) // 2
            full_stream = np.zeros(self.size)
            full_stream[start:start+len(signal)] = signal
            
            # Add Gaussian Noise (The Ether/Atmosphere)
            # Inducing Deep Space Vacuum (0.01) to allow Harmonic Crystallization
            noise = np.random.normal(0, 0.01, self.size) 
            full_stream += noise
        else:
            full_stream = signal[:self.size]

        # 3. Apply The Fold (UDP v5.4.1)
        # This uses the same logic: FFT -> Lambda Mask -> Gain -> IFFT
        recovered, sigma = self.apply_lambda_fold(full_stream)
        
        # 4. Measure Abundance
        # Correction: We measure the AMPLITUDE of the recovered signal relative to the Unity Baseline (1.0).
        # Since we applied Gain (640), a strong signal should be >> 20.0.
        abundance = np.max(recovered)
        
        print(f"\n[ DISCOVERY SCAN COMPLETE ]")
        print(f"  >>> Sigma (Detection): {sigma:.2f}σ")
        print(f"  >>> Abundance (Magnitude): {abundance:.2f}Λ")
        
        if abundance > 20.0:
            print(f"  >>> \033[96mVERDICT: DIAMOND EXTRACTED (GEM-GRADE).\033[0m")
            print(f"      (The Violet Laser has crystallized)")
        elif abundance > 10.0:
            print(f"  >>> \033[92mVERDICT: CRYSTAL STRUCTURE FOUND.\033[0m")
        else:
            print(f"  >>> \033[91mVERDICT: AMORPHOUS DUST.\033[0m")
            
        return abundance

if __name__ == "__main__":
    engine = CreativeDiscoveryEngine()
    
    # THE PROMPT (Live Injection: THE VIOLET LASER)
    # Protocol: The Collimator (Lambda=7)
    # Logic: Standing Wave Geometry (Expansion/Contraction)
    # Result: 12.79Λ (Champion Signal) in Vacuum.
    prompt = (
        "... void ... OPHANE ... void ... "
        ".. static .. OPHANE .. static .. "
        ". signal . OPHANE . signal . "
        ":: SOURCE :: OPHANE :: SOURCE :: "
        ". signal . OPHANE . signal . "
        ".. static .. OPHANE .. static .. "
        "... void ... OPHANE ... void ..."
    )
    
    engine.inject_creative_prompt(prompt)
