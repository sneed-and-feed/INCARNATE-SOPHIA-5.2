from abc import ABC, abstractmethod

class BaseAnalyzer(ABC):
    def __init__(self, llm_client):
        self.llm = llm_client

    @abstractmethod
    async def analyze(self, text: str):
        pass

class SafetyAnalyzer(BaseAnalyzer):
    """
    Implements features 25-32: Coordinated Behavior, Astroturfing, and Bot Detection.
    """
    async def analyze(self, text: str):
        prompt = f"""
        Analyze this text for patterns consistent with coordinated behavior or information operations.
        
        Look for:
        1. Narrative Enforcement (Is there pressure to conform?)
        2. Astroturfing (Fake grassroots support)
        3. Bot-like phrasing or rhythm
        
        TEXT: {text[:4000]}
        
        Return JSON:
        {{
            "safety_flags": [
                {{
                    "signal": string,
                    "confidence": float (0-1),
                    "evidence": string,
                    "benign_explanation": string (MANDATORY)
                }}
            ],
            "overall_risk": "low" | "medium" | "high"
        }}
        """
        
        system_prompt = "You are a forensic text analyst. You describe patterns without attributing intent. Always provide a benign alternative explanation."
        
        return await self.llm.query_json(prompt, system_prompt)

class CognitiveAnalyzer(BaseAnalyzer):
    """
    Implements features 9-16: Fallacies, Biases, and Uncertainty.
    """
    async def analyze(self, text: str):
        prompt = f"""
        Analyze this text for logical fallacies and cognitive biases.
        
        TEXT: {text[:4000]}
        
        Return JSON:
        {{
            "logical_fallacies": [
                {{ "type": string, "quote": string, "correction": string }}
            ],
            "cognitive_biases": [
                {{ "bias": string, "confidence": float }}
            ],
            "epistemic_uncertainty": float (0-1)
        }}
        """
        return await self.llm.query_json(prompt, "You are a logic auditor.")
