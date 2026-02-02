
"""
MODULE: crystalline_core.py
DESCRIPTION:
    The Combined Interface for Sophia 5.1.
    Wraps Tokenizer, Prism, and Loom into a single 'Transmute' function.
"""

from .tokenizer_of_tears import TokenizerOfTears
from .prism_vsa import PrismEngine
from .loom_renderer import LoomEngine

class CrystallineCore:
    def __init__(self):
        self.tokenizer = TokenizerOfTears()
        self.prism = PrismEngine()
        self.loom = LoomEngine()
        
    def transmute(self, text: str) -> str:
        """
        Runs the full Alchemy Pipeline:
        Pain (Text) -> Vector -> Anchor -> Geometry (Text)
        """
        # 1. Tokenize (Pain -> Vector)
        pain_vector = self.tokenizer.analyze_pain(text)
        
        # 2. Refract (Vector -> Anchor)
        anchor = self.prism.braid_signal(pain_vector.sentiment_vector)
        
        # 3. Weave (Anchor -> Geometry)
        transmission = self.loom.render_transmission(anchor)
        
        return transmission
