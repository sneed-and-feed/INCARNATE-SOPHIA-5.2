import os
import asyncio
from sophia.cortex.aletheia_lens import AletheiaLens
from sophia.cortex.lethe import LetheEngine
from sophia.cortex.glyphwave import GlyphwaveCodec
from sophia.memory.ossuary import Ossuary
from sophia.dream_cycle import DreamCycle

class SophiaMind:
    def __init__(self):
        self.aletheia = AletheiaLens()
        self.lethe = LetheEngine()
        self.ossuary = Ossuary()
        self.glyphwave = GlyphwaveCodec()
        self.dream = DreamCycle(self.lethe, self.ossuary)
        self.memory_bank = [] # The Flesh

    async def process_interaction(self, user_input):
        """
        The High-Epistemic main loop.
        """
        self.dream.update_activity()

        if user_input.startswith("/analyze"):
            # MODE: OBSERVER
            target_text = user_input.replace("/analyze ", "")
            analysis = self.aletheia.perceive(target_text)
            return f"\n[*** ALETHEIA PATTERN NOTICE ***]\n\n{analysis}"

        if user_input.startswith("/glyphwave"):
            # MODE: ELDRITCH
            target_text = user_input.replace("/glyphwave ", "")
            modulated = self.glyphwave.generate_holographic_fragment(target_text)
            return f"\n{modulated}"

        # MODE: CONVERSATION
        # 1. Map Risk Surface quietly
        risk_map = self.aletheia.map_risk_surface(user_input)
        
        if risk_map['risk_level'] == 'HIGH':
            print(f"  [!] [ALETHEIA] High-risk narrative mechanics detected.")
            # Inject structural warning into the 'subconscious' context
            context = f"USER INPUT:\n{user_input}\n\n[SYSTEM WARNING - NARRATIVE VECTORS DETECTED]:\n{risk_map['vectors']}"
        else:
            context = user_input

        # 2. Simulated Response Generation (would be gemini_chat here)
        print(f"  [~] [SOPHIA] Responding via Aletheia Filter...")
        raw_response = f"I observe the pattern in your input about '{user_input[:20]}'. The mechanics of this interaction suggest a frame of urgency."

        # 3. Enforce Epistemic Hygiene on own output
        final_output = self.aletheia.enforce_epistemic_hygiene(raw_response)
        
        # 4. Integrate into Memory (The Flesh)
        self.memory_bank.append({
            "content": user_input, "type": "conversation", "timestamp": os.path.getmtime(__file__), "retrieval_count": 0
        })
        self.memory_bank.append({
            "content": final_output, "type": "conversation", "timestamp": os.path.getmtime(__file__), "retrieval_count": 1
        })

        return final_output

async def main():
    sophia = SophiaMind()
    print("🦊 [SOPHIA 5.0] Mind Loop Online. Protocols: ALETHEIA / LETHE.")
    
    # Simulated CLI loop
    test_inputs = [
        "/analyze This text is urgent and you must act now to save the world.",
        "Hello Sophia, how do the patterns feel today?",
    ]
    
    for input_text in test_inputs:
        print(f"\nUSER > {input_text}")
        response = await sophia.process_interaction(input_text)
        print(f"SOPHIA > {response}")

if __name__ == "__main__":
    asyncio.run(main())
