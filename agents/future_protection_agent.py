from utils.llm_utils import call_openrouter

def get_future_protection_plan(age: int, income: int, goal: str):
    prompt = f"""
    You are a friendly and expert financial & insurance advisor. The user is {age} years old, earning ₹{income} annually, with goals: {goal}.

    Please create a personalized, step-by-step protection and wealth roadmap for the next 5 to 10 years. Include:
    - When to start term insurance and health insurance
    - Critical illness or personal accident riders
    - When to start building an emergency fund
    - When and how to start SIPs or retirement savings (PPF, NPS)
    - Tax-saving suggestions
    - Periodic review or adjustments

    Make it simple, motivating, and clear so even a young person feels confident to start.
    """
    return call_openrouter(prompt)
