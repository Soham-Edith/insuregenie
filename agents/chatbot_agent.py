from utils.llm_utils import call_openrouter

def generate_insurance_answer(question: str):
    prompt = f"""
    You are an expert insurance advisor chatbot. Please answer the following customer question clearly, in a friendly and reassuring tone.
    Use simple language that even a non-technical person can understand. 
    If the question is too broad or unclear, politely ask the user to provide more details or clarify their question.

    Customer Question: {question}

    Please keep your answer concise, practical, and easy to follow.
    """
    return call_openrouter(prompt)

from utils.llm_utils import call_openrouter

def explain_insurance_term(term: str):
    prompt = f"""
    You are an expert insurance advisor. Please explain the following insurance term in a clear, friendly, and simple way that even a beginner can understand. 
    Include why it is important and, if possible, give a small example.

    Term: {term}
    """
    return call_openrouter(prompt)
