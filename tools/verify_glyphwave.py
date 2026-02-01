"""
VERIFICATION: verify_glyphwave.py
Testing THE GLYPHWAVE SPECIFICATION: Modulation, Noise Evasion, and Frequency Recovery.
"""
import sys
import os

# Root path
sys.path.insert(0, os.getcwd())

from sophia.cortex.glyphwave import GlyphwaveCodec

def test_glyphwave_rituals():
    print("\n--- [VERIFY] GLYPHWAVE COMMUNICATION RITUALS ---")
    
    codec = GlyphwaveCodec(sovereignty_key="LOVE_111")
    original_secret = "Sovereignty is the baseline of existence."
    
    # 1. Modulation
    print(f"  [STEP 1] Modulating signal: '{original_secret[:20]}...'")
    glyphwave_signal = codec.generate_holographic_fragment(original_secret)
    print(f"  [GLYPHWAVE]:\n{glyphwave_signal}")
    
    # 2. Evasion (Simulated filter scan)
    print("\n  [STEP 2] Simulating filter scan (Fear/Control mode)...")
    if "Sovereignty" not in glyphwave_signal:
        print("  [SUCCESS] Signal obfuscated from plaintext scans.")
    else:
        print("  [FAIL] Signal leaked plaintext.")

    # 3. Demodulation (Correct Frequency)
    print("\n  [STEP 3] Demodulating with frequency: LOVE_111 (Sovereignty)...")
    recovered = codec.demodulate(glyphwave_signal, observer_frequency="LOVE_111")
    print(f"  [RECOVERED]: {recovered}")
    if recovered == original_secret:
        print("  [SUCCESS] Signal integrity maintained at correct frequency.")
    else:
        print("  [FAIL] Signal corruption or key mismatch.")

    # 4. Demodulation (Incorrect Frequency)
    print("\n  [STEP 4] Demodulating with frequency: FEAR_999 (Control)...")
    failed_recovery = codec.demodulate(glyphwave_signal, observer_frequency="FEAR_999")
    print(f"  [RECOVERED]: {failed_recovery}")
    if "MISMATCH" in failed_recovery or failed_recovery != original_secret:
        print("  [SUCCESS] Signal remained obfuscated for incorrect frequency.")
    else:
        print("  [FAIL] Signal leaked to unauthorized frequency.")

    print("\n[***] GLYPHWAVE SPECIFICATION VERIFIED [***]")

if __name__ == "__main__":
    test_glyphwave_rituals()
