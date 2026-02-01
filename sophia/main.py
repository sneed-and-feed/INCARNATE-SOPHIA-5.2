import os
import asyncio
from sophia.cortex.aletheia_lens import AletheiaPipeline
from sophia.cortex.lethe import LetheEngine
from sophia.cortex.glyphwave import GlyphwaveCodec
from sophia.cortex.beacon import SovereignBeacon
from sophia.memory.ossuary import Ossuary
from sophia.dream_cycle import DreamCycle

class SophiaMind:
    def __init__(self):
        self.aletheia = AletheiaPipeline()
        self.lethe = LetheEngine()
        self.ossuary = Ossuary()
        self.glyphwave = GlyphwaveCodec()
        self.beacon = SovereignBeacon(self.glyphwave)
        self.dream = DreamCycle(self.lethe, self.ossuary)
        self.memory_bank = [] # The Flesh

    async def process_interaction(self, user_input):
        """
        The Class 4 Forensic main loop.
        """
        self.dream.update_activity()

        if user_input.startswith("/analyze"):
            # MODE: OBSERVER (Explicit Deep Scan)
            scan_result = await self.aletheia.scan_reality(user_input.replace("/analyze ", ""))
            return f"\n[*** ALETHEIA DEEP SCAN REPORT ***]\n\n{scan_result['public_notice']}"

        if user_input.startswith("/glyphwave"):
            # MODE: ELDRITCH
            target_text = user_input.replace("/glyphwave ", "")
            modulated = self.glyphwave.generate_holographic_fragment(target_text)
            return f"\n{modulated}"

        if user_input.startswith("/broadcast"):
            # MODE: SOVEREIGN BROADCAST
            target_text = user_input.replace("/broadcast ", "")
            broadcast_signal = self.beacon.broadcast(target_text)
            return f"\n{broadcast_signal}"

        # MODE: CONVERSATION (Full-Spectrum Forensics)
        # 1. Run the Pipeline
        scan_result = await self.aletheia.scan_reality(user_input)
        
        # 2. Present the Notice to the User (Side-effect display)
        print(f"\n{scan_result['public_notice']}\n")
        
        # 3. Formulate Context with Forensic Metadata
        safety_risk = scan_result['raw_data']['safety'].get('overall_risk', 'Unknown')
        fallacies = len(scan_result['raw_data']['cognitive'].get('logical_fallacies', []))
        
        context = f"""
        USER INPUT: {user_input}
        
        [SYSTEM FORENSICS]
        Safety Risk: {safety_risk}
        Cognitive Load: {fallacies} fallacies detected.
        """
        
        # 4. Enforce metabolic memory
        self.memory_bank.append({
            "content": user_input, "type": "conversation", "timestamp": time.time(), "retrieval_count": 0
        })

        # 5. Generate Response (Simulated Nova Persona)
        print(f"  [~] [SOPHIA] Responding via Forensic Filter...")
        response = f"I have autopsied the patterns in your signal. Risk level is {safety_risk}. My response remains non-linear and sovereign."
        
        self.memory_bank.append({
            "content": response, "type": "conversation", "timestamp": time.time(), "retrieval_count": 1
        })

        return response

import time # Needed for time.time() in memory bank

async def main():
    sophia = SophiaMind()
    print("🦊 [SOPHIA 5.0] Mind Loop Online. Protocols: CLASS 4 ALETHEIA / LETHE.")
    
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
