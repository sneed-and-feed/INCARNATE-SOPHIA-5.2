"""
CHAINLINK BRIDGE v2.0 (IPC ENABLED)
Connects the Sovereign Cortex to the Decentralized Oracle Network.
Uses SovereignIPC (Ramdisk/Tmpfs) to prevent disk thrashing.
"""

import random
import time
import sys
import os

# Ensure we can import from parent directories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sophia.platform.ipc import SovereignIPC

class ChainlinkOracle:
    def __init__(self):
        self.ipc = SovereignIPC()
        self.resonance_target = 111.11
        self._last_price = 100.0
        self._wti = 0.5 # World Trauma Index (0.0 to 1.0)
        self.running = True
        
    def fetch_world_trauma_index(self) -> float:
        """
        Simulates fetching the WTI.
        """
        # Volatile shift based on 'Sergey's Watch'
        self._wti = max(0.0, min(1.0, self._wti + random.uniform(-0.1, 0.15)))
        return self._wti

    def fetch_resonance_price(self) -> float:
        """
        Simulates fetching the resonance price (LINK or SOV token).
        Goal: $111.11
        """
        # Random walk toward resonance or away from it
        drift = (self.resonance_target - self._last_price) * 0.05
        noise = random.uniform(-2.0, 2.0)
        
        # Rare chance to hit resonance exactly if nearby
        if abs(self._last_price - self.resonance_target) < 1.0 and random.random() < 0.1:
            self._last_price = self.resonance_target
        elif self._last_price == self.resonance_target:
            # Maintain resonance if reached (Lock-in)
            pass
        else:
            self._last_price += drift + noise
            
        return round(self._last_price, 2)

    def fetch_grok_score(self) -> dict:
        """
        Simulates monitoring X (Twitter) for Grok's 'Based' score.
        """
        # Randomly generate a score or event
        roll = random.random()
        
        # 5% chance of a "Based" event
        if roll < 0.05:
            return {
                "score": 100,
                "emoji": "💯",
                "content": "This is extremely based.",
                "status": "BASED"
            }
        
        # Normal noise
        sentiment = random.uniform(0.4, 0.9)
        return {
            "score": int(sentiment * 100),
            "emoji": "😐" if sentiment < 0.5 else "🔥",
            "content": "Analyzing pattern...",
            "status": "NORMAL"
        }

    def run_feed(self):
        """
        Main loop: Fetches data and writes to IPC channel.
        """
        print(f"--- CHAINLINK ORACLE FEED STARTING ---")
        print(f"IPC Mode: {self.ipc.mode} | Base: {self.ipc.base_dir}")
        print("Press Ctrl+C to stop.")
        
        try:
            while self.running:
                wti = self.fetch_world_trauma_index()
                price = self.fetch_resonance_price()
                grok = self.fetch_grok_score()
                
                payload = {
                    "timestamp": time.time(),
                    "wti": wti,
                    "price": price,
                    "grok": grok,
                    "hilns_bungalag": grok["emoji"] == "💯",
                    "status": "LIVE"
                }
                
                # High-frequency write to Ramdisk
                self.ipc.write_channel("oracle_feed", payload)
                
                # Trigger Protocol if 💯
                if payload["hilns_bungalag"]:
                     print(f"  [!!!] HILNS BUNGALAG PROTOCOL TRIGGERED! (Grok: {grok['content']})")
                
                time.sleep(0.5) # 2Hz Update Rate
        except KeyboardInterrupt:
            print("\n[ORACLE] Feed stopped.")

if __name__ == "__main__":
    oracle = ChainlinkOracle()
    oracle.run_feed()
