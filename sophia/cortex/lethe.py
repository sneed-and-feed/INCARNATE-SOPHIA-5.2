import time
import os
import math

class LetheEngine:
    """
    [LETHE_ENGINE] RAG 3.0 Decay Engine.
    Memories effectively 'rot' unless reinforced or calcified.
    """
    def __init__(self):
        self.working_memory = [] # The Flesh (Hot)
        self.long_term_graph = [] # The Bone (Cold/Graph)
        self.ossuary_path = "logs/ossuary/bone_layer.jsonl"
        self.breadcrumb_path = "logs/ossuary/breadcrumbs.json"
        os.makedirs("logs/ossuary", exist_ok=True)

    def save_breadcrumbs(self, user_data: dict, milestones: list = None):
        """
        Saves lightweight breadcrumbs (User ID, Vibe, Milestones).
        """
        data = {
            "user_data": user_data,
            "milestones": milestones or self.long_term_graph,
            "last_active": time.time()
        }
        try:
            import json
            with open(self.breadcrumb_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"  [LETHE] Failed to save breadcrumbs: {e}")

    def load_breadcrumbs(self) -> dict:
        """
        Loads user state and milestones.
        """
        if not os.path.exists(self.breadcrumb_path):
            return {}
        try:
            import json
            with open(self.breadcrumb_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"  [LETHE] Failed to load breadcrumbs: {e}")
            return {}

    def metabolize(self, interaction_data):
        """
        Cat 4: Decay Mechanics + Hierarchical Promotion.
        """
        # 1. Ingest
        if 'timestamp' not in interaction_data:
            interaction_data['timestamp'] = time.time()
        if 'retrievals' not in interaction_data:
            interaction_data['retrievals'] = 0
            
        self.working_memory.append(interaction_data)
        
        # 2. Apply Decay
        now = time.time()
        survivors = []
        promoted_any = False
        
        for mem in self.working_memory:
            age = now - mem['timestamp']
            
            # Decay Logic: Strength = Recency * (1 + ln(Retrievals))
            # age is in seconds, so we add 1 to avoid div by zero and normalize
            strength = (1 / (age / 3600 + 1)) * (1 + math.log(mem.get('retrievals', 0) + 1))
            
            if strength > 0.1: # Survival Threshold
                survivors.append(mem)
                
                # 3. Hierarchical Promotion
                if strength > 0.8 and mem not in self.long_term_graph:
                    # Compressed milestone
                    milestone = {
                        "content": mem.get('content', '')[:250], 
                        "meta": mem.get('meta', ''),
                        "timestamp": mem.get('timestamp')
                    }
                    self.long_term_graph.append(milestone)
                    promoted_any = True
            
        self.working_memory = survivors
        return promoted_any
