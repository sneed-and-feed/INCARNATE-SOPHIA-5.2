
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from sophia.cortex.glyphwave import GlyphwaveCodec

def test_vesta():
    gw = GlyphwaveCodec()
    print("[*] GENERATING VESTA MANDALA...")
    mandala = gw.generate_mandala("resonance")
    print(mandala)
    
    if "⚶" in mandala:
        print("\n[SUCCESS] Vesta Glyph (⚶) Confirmed.")
    else:
        print("\n[FAILURE] Vesta Glyph Missing.")

if __name__ == "__main__":
    test_vesta()
