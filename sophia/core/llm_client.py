import os
import google.generativeai as genai
import json
import asyncio
from dataclasses import dataclass

@dataclass
class LLMConfig:
    model_name: str = "gemini-1.5-flash"
    temperature: float = 0.1

class GeminiClient:
    def __init__(self):
        # Using the God-Mode environment variable
        api_key = os.getenv("GOOGLE_AI_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            # Fallback for playground environment if needed
            api_key = "REDACTED" # This will be handled by the environment in production
            
        genai.configure(api_key=api_key)
        
    async def query_json(self, prompt: str, system_prompt: str = None) -> dict:
        """
        Forces Gemini to output strict JSON for the analysis pipeline.
        """
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro", # Use Pro for deep analysis
            generation_config={"response_mime_type": "application/json"}
        )
        
        full_prompt = f"{system_prompt}\n\nUSER PROMPT:\n{prompt}" if system_prompt else prompt
        
        try:
            # Run in executor to make the sync Gemini call async
            loop = asyncio.get_running_loop()
            response = await loop.run_in_executor(None, lambda: model.generate_content(full_prompt))
            return json.loads(response.text)
        except Exception as e:
            print(f"[GEMINI ADAPTER ERROR] {e}")
            return {"error": str(e)}
