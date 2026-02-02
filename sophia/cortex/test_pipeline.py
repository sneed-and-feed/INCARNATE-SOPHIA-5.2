
"""
TEST: test_pipeline.py
DESCRIPTION:
    End-to-End Verification of the Sophia 5.1 Crystalline Core.
    Pipeline: Input -> Tokenizer -> Prism -> Loom -> Output.
"""

from tokenizer_of_tears import TokenizerOfTears
from prism_vsa import PrismEngine
from loom_renderer import LoomEngine

def run_pipeline_test():
    print("### [ SOPHIA 5.1: CRYSTALLINE CORE TEST ]")
    
    # 1. Initialize Stack
    tokenizer = TokenizerOfTears()
    prism = PrismEngine()
    loom = LoomEngine()
    
    # 2. Test Inputs
    inputs = [
        "System falling apart, help me!",  # Should trigger Descent/Chaos -> LANDING?
        "I am lost in the silence.",       # Should trigger Void -> VOID/ORBIT
        "Everything is broken crash.",     # Should trigger Descent -> LANDING
        "Waiting for signal."              # Should trigger Wait -> WAIT
    ]
    
    for txt in inputs:
        print(f"\nINCOMING: \"{txt}\"")
        
        # A. Tokenize
        pain_vector = tokenizer.analyze_pain(txt)
        print(f"  [1] VECTOR: {pain_vector.sentiment_vector} (Urgency: {pain_vector.urgency})")
        
        # B. Prism
        anchor = prism.braid_signal(pain_vector.sentiment_vector)
        print(f"  [2] ANCHOR: {anchor.upper()}")
        
        # C. Loom
        transmission = loom.render_transmission(anchor)
        print(f"  [3] OUTPUT: \033[95m{transmission}\033[0m")

if __name__ == "__main__":
    run_pipeline_test()
