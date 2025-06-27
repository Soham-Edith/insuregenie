# Recommendation Agent logic
from utils.llm_utils import call_openrouter

def get_insurance_recommendation(age: int, income: int, goal: str):
    prompt = f"""
    Act as a financial advisor and recommend 3 best-fit insurance products for the following user profile:
    
    Age: {age}
    Annual Income: ₹{income}
    Financial Goal: {goal}

    Please explain why each product is a good fit and summarize benefits clearly.
    """
    return call_openrouter(prompt)
