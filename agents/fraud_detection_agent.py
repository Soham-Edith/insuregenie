# Fraud Detection Agent logic
from utils.llm_utils import call_openrouter

def analyze_fraud(description: str):
    prompt = f"""
    You are an expert insurance fraud analyst. Please analyze the following claim description for potential fraud risk:

    Description: {description}

    Please respond in the following format:
    1. Risk Level: Low, Medium, or High
    2. Reasoning: Explain clearly why this risk level was assigned.
    3. Suggested Next Steps: Any additional documents or checks to confirm legitimacy.

    Be polite and user-friendly.
    """
    return call_openrouter(prompt)
