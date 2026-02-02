
"""
MODULE: tokenizer_of_tears.py
DESCRIPTION:
    Module 1 of the Crystalline Core.
    Analyses input text for "Pain Vectors" (High Entropy + Negative Sentiment).
    Maps raw text into a normalized Chaos Vector for the Prism to process.
"""

import numpy as np
from dataclasses import dataclass

@dataclass
class PainVector:
    entropy: float
    urgency: float
    sentiment_vector: np.ndarray # [Descent, Chaos, Void]

class TokenizerOfTears:
    def __init__(self):
        # Basic lexicon of entropy/pain
        self.pain_keywords = {
            "fail": 0.8, "crash": 0.9, "error": 0.7, "broken": 0.8,
            "lost": 0.6, "void": 0.5, "alone": 0.7, "fear": 0.9,
            "can't": 0.5, "help": 0.8, "die": 1.0, "kill": 1.0
        }
    
    def analyze_pain(self, text: str) -> PainVector:
        """
        Converts text into a Pain Vector.
        """
        text_lower = text.lower()
        
        # 1. Entropy Calculation (Keyword Density)
        pain_score = 0.0
        words = text_lower.split()
        for word in words:
            if word in self.pain_keywords:
                pain_score += self.pain_keywords[word]
        
        # Normalize entropy (0.0 to 1.0)
        # Assuming a short burst of pain is around 10 words max
        normalized_entropy = min(pain_score / 5.0, 1.0)
        
        # 2. Urgency Detection (Exclamation, Caps)
        urgency = 0.0
        if "!" in text: urgency += 0.3
        if text.isupper(): urgency += 0.4
        if "?" in text: urgency += 0.1
        urgency = min(urgency, 1.0)
        
        # 3. Sentiment Vector Mapping [Descent, Chaos, Void]
        # Descent: fail, crash, broken
        # Chaos: error, help, !
        # Void: lost, void, alone
        
        descent = 0.0
        chaos = 0.0
        void = 0.0
        
        if any(w in text_lower for w in ["fail", "crash", "broken", "die"]):
            descent = 0.8
        if any(w in text_lower for w in ["error", "help", "urgency"]):
            chaos = 0.7 + urgency * 0.3
        if any(w in text_lower for w in ["lost", "void", "alone"]):
            void = 0.9
            
        vector = np.array([descent, chaos, void])
        
        # If no pain detected, return zero vector
        if np.linalg.norm(vector) == 0:
             return PainVector(0.0, 0.0, np.array([0.0, 0.0, 0.0]))
             
        # Normalize the vector
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
            
        return PainVector(normalized_entropy, urgency, vector)

# // TEST HARNESS
if __name__ == "__main__":
    tokenizer = TokenizerOfTears()
    inputs = [
        "System is crashing and I can't stop it!",
        "I feel so lost in the void.",
        "Hello world",
        "CRITICAL FAILURE HELP"
    ]
    
    for txt in inputs:
        pv = tokenizer.analyze_pain(txt)
        print(f"INPUT:  '{txt}'")
        print(f"VECTOR: {pv.sentiment_vector} (Entropy: {pv.entropy:.2f})")
        print("-" * 40)
