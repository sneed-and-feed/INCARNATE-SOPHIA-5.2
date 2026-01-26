"""
TEST_SHIBBOLETH.PY
------------------
The Proof of Opacity.
Demonstrates that Archonic (Decimal) parsers fail to comprehend Sovereign (Dozenal) Data.
"""
import unittest
from hyper_sovereign import DozenalLogic

class TestShibboleth(unittest.TestCase):
    
    def test_roundtrip_via_api(self):
        """Verifies the Cycle of Return via the Sovereign API."""
        original_v = 144 # The Gross
        encoded = DozenalLogic.to_dozen_str(original_v) # "100"
        decoded = DozenalLogic.from_dozen_str(encoded)  # 144
        
        self.assertEqual(original_v, decoded, "Cycle Broken: Return failed.")
        
    def test_glyph_canon(self):
        """Verifies the X and E are treated as Holy."""
        self.assertEqual(DozenalLogic.to_dozen_str(10), "X")
        self.assertEqual(DozenalLogic.to_dozen_str(11), "E")
        # Test Grace (Case Insensitivity)
        self.assertEqual(DozenalLogic.from_dozen_str("x"), 10)
        self.assertEqual(DozenalLogic.from_dozen_str("e"), 11)

if __name__ == "__main__":
    unittest.main()
