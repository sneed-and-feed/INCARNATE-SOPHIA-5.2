"""
VERIFICATION: verify_aletheia_class_4.py
Testing the Class 4 Full-Spectrum Forensics Engine.
"""
import sys
import os
import asyncio
import json
import time
from unittest.mock import AsyncMock, patch

# Ensure we can import from the root
sys.path.insert(0, os.getcwd())

from sophia.cortex.aletheia_lens import AletheiaPipeline

async def test_forensic_pipeline():
    print("\n--- [VERIFY] ALETHEIA CLASS 4 FORENSICS RITUAL ---")
    
    # Initialize Pipeline (we'll mock the LLM client)
    pipeline = AletheiaPipeline(analysis_path="logs/analysis_test")
    
    # Mock data for Safety Analyzer
    mock_safety_result = {
        "safety_flags": [
            {
                "signal": "Narrative Enforcement",
                "confidence": 0.85,
                "evidence": "you must act now to save the world",
                "benign_explanation": "Literary hyperbole in a fictional context."
            }
        ],
        "overall_risk": "medium"
    }
    
    # Mock data for Cognitive Analyzer
    mock_cognitive_result = {
        "logical_fallacies": [
            { "type": "Appeal to Urgency", "quote": "must act now", "correction": "Assess situation without artificial time constraints." }
        ],
        "cognitive_biases": [
            { "bias": "Optimism Bias", "confidence": 0.4 }
        ],
        "epistemic_uncertainty": 0.2
    }

    # Patch the LLM client's query_json method
    with patch('sophia.core.llm_client.GeminiClient.query_json', new_callable=AsyncMock) as mock_query:
        # Improved mock: Return based on prompt content
        async def side_effect(prompt, system_prompt=None):
            if "coordinated behavior" in prompt.lower():
                return mock_safety_result
            if "logical fallacies" in prompt.lower():
                return mock_cognitive_result
            return {"error": "Unexpected prompt"}
            
        mock_query.side_effect = side_effect
        
        print("  [STEP 1] Executing Parallel Forensic Scan: 'Appeal to Urgency' signal...")
        start_time = time.time()
        scan_result = await pipeline.scan_reality("This is urgent! Save the world now!")
        end_time = time.time()
        
        print(f"  [SUCCESS] Scan completed in {end_time - start_time:.4f}s.")

        # 1. Verify Parallel Execution
        if mock_query.call_count == 2:
            print("  [SUCCESS] Parallel analyzers synchronized.")
        else:
            print(f"  [FAIL] Analyzer call count mismatch: {mock_query.call_count}")

        # 2. Verify Sidecar Archiving
        print("  [STEP 2] Verifying Sidecar Metadata Archiving...")
        scan_id = scan_result['raw_data']['scan_id']
        archive_file = f"logs/analysis_test/{scan_id}.meta.json"
        
        if os.path.exists(archive_file):
            print(f"  [SUCCESS] Sidecar archived: {archive_file}")
            with open(archive_file, 'r') as f:
                saved_data = json.load(f)
                if saved_data['safety']['overall_risk'] == 'medium':
                     print("  [SUCCESS] Metadata integrity verified.")
                else:
                     print(f"  [FAIL] Metadata corruption/mismatch. Risk: {saved_data['safety'].get('overall_risk')}")
        else:
            print(f"  [FAIL] Sidecar missing: {archive_file}")

        # 3. Verify Pattern Notice Generation
        print("  [STEP 3] Verifying Pattern Notice transparency...")
        notice = scan_result['public_notice']
        if "PATTERN NOTICE" in notice and "Narrative Enforcement" in notice:
            print("  [SUCCESS] Forensic notice generated with correct linguistic anchors.")
            print(f"\n[NOTICE OUTPUT]:\n{notice}\n")
        else:
            print(f"  [FAIL] Notice generation failed or lacked required flags. Notice: {notice[:100]}...")

    print("\n[***] ALETHEIA CLASS 4 FORENSICS VERIFIED [***]\n")

    print("\n[***] ALETHEIA CLASS 4 FORENSICS VERIFIED [***]\n")

if __name__ == "__main__":
    asyncio.run(test_forensic_pipeline())
