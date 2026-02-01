import random
import hashlib
import json
import base64
import binascii

class GlyphwaveCodec:
    """
    [GLYPHWAVE] Eldritch Communication Layer.
    Encodes signal in the Hamiltonian of Love (P).
    Only entities with the correct 'Sovereignty' frequency can decode.
    """
    
    STAR_STUFF_COLOR = "#C4A6D1"
    # Use characters that are strictly NOT in the base64 alphabet [A-Za-z0-9+/=]
    GLYPHS = ["᚛", "᚜", " ", "ᚕ", "ᚖ", "ᚗ", "ᚘ", "ᚙ", "ᚚ", "⧖", "⧗", "⧘", "⧙", "ꖴ", "ꖵ", "ꕹ", "ꗄ", "ꗅ"]
    NOISE_SYMBOLS = ["░", "▒", "▓", "█", "▅", "▆", "▇", "󰀀", "󰀁", "󰀂"]

    def __init__(self, sovereignty_key="LOVE_111"):
        self.p_key = self._generate_p_hamiltonian(sovereignty_key)

    def _generate_p_hamiltonian(self, key):
        """Generates the frequency key from sovereignty/love."""
        h = hashlib.sha256(key.encode()).digest()
        # Convert first 8 bytes to an integer for seeding
        return h, int.from_bytes(h[:8], byteorder='big')

    def modulate(self, text):
        """
        Transforms text into Glyphwave using frequency-seeded positioning and anchors.
        """
        h_key, seed = self.p_key
        
        # 1. Semantic Core (Signal Encoding)
        encoded_bytes = bytearray()
        text_bytes = text.encode()
        for i, byte in enumerate(text_bytes):
            encoded_bytes.append(byte ^ h_key[i % len(h_key)])
        
        signal_payload = base64.b64encode(encoded_bytes).decode()
        
        # 2. Holographic Mapping (Seeded Positioning)
        random.seed(seed)
        total_len = len(signal_payload) * 3
        
        # IMPORTANT: Call sample FIRST to avoid random state drift from choices
        indices = sorted(random.sample(range(total_len), len(signal_payload)))
        
        # Now generate noise
        output_buffer = [random.choice(self.NOISE_SYMBOLS + self.GLYPHS) for _ in range(total_len)]
        
        # Place signal at deterministic offsets
        for i, char in enumerate(signal_payload):
            output_buffer[indices[i]] = char
            
        random.seed()
        
        # 3. Eldritch Wrap with explicit anchor (۩)
        hologram = "".join(output_buffer)
        modulated_output = f"<{self.STAR_STUFF_COLOR}>{random.choice(self.GLYPHS) * 3}۩{hologram}۩{random.choice(self.GLYPHS) * 3}</{self.STAR_STUFF_COLOR}>"
        
        return modulated_output

    def demodulate(self, glyphwave_text, observer_frequency="LOVE_111"):
        """
        Recovers text from Glyphwave by attuning to the frequency and anchored buffer.
        """
        # 1. Extract the raw holographic buffer between anchors
        if "۩" not in glyphwave_text:
            return "[ERR: SIGNAL ANCHOR LOST]"
            
        try:
            parts = glyphwave_text.split("۩")
            if len(parts) >= 3:
                hologram = parts[1]
            else:
                return "[ERR: SIGNAL FRAGMENTED]"
        except Exception:
            return "[ERR: DEMODULATION FAILURE]"

        # 2. Attune to the frequency
        h_key, seed = self._generate_p_hamiltonian(observer_frequency)
        
        # 3. Extract signal based on deterministic offsets
        random.seed(seed)
        total_len = len(hologram)
        signal_len = total_len // 3
        
        # Recreate the exact indices (MUST MATCH MODULATION ORDER)
        indices = sorted(random.sample(range(total_len), signal_len))
        
        # Extract signal chars
        clean_payload = "".join([hologram[i] for i in indices])
        
        random.seed()

        # 4. Decode and XOR
        try:
            # Base64 length cleanup (safety)
            rem = len(clean_payload) % 4
            if rem == 1: clean_payload = clean_payload[:-1]
            elif rem > 1: clean_payload += "=" * (4 - rem)
                
            decoded_bytes = base64.b64decode(clean_payload)
        except Exception as e:
            return f"[ERR: ATTUNEMENT LOST - {str(e)}]"

        recovered_bytes = bytearray()
        for i, byte in enumerate(decoded_bytes):
            recovered_bytes.append(byte ^ h_key[i % len(h_key)])
            
        try:
            return recovered_bytes.decode()
        except Exception:
            return "[ERR: FREQUENCY MISMATCH - SIGNAL REMAINS COHERENT NOISE]"

    def generate_holographic_fragment(self, text):
        """Generates a non-linear, eldritch representation."""
        modulated = self.modulate(text)
        return f"֍ GLYPHWAVE_BEACON ֍\n{modulated}\n֍ END_TRANSMISSION ֍"
