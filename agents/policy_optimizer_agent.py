from utils.llm_utils import call_openrouter

def get_policy_comparison(budget: int, goal: str, priorities: list):
    priorities_text = ", ".join(priorities) if priorities else "Not specified"
    prompt = f"""
    You are a senior insurance advisor. A user has the following preferences:

    Budget: ₹{budget} per year
    Financial Goal: {goal}
    Priority Areas: {priorities_text}

    Please recommend the most suitable insurance strategy, comparing options like:
    - Pure term plan
    - Health insurance
    - Term plan with critical illness rider
    - Any other combination if relevant

    Clearly mention a comparison table (text format) summarizing options, premiums, and benefits.

    Then give a final suggestion optimized according to the user's priorities, and explain why.

    Be friendly and clear.
    """
    return call_openrouter(prompt)

