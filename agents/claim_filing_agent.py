from utils.llm_utils import call_openrouter

def process_claim(claim_type: str, amount: int, description: str):
    prompt = f"""
    You are an expert insurance claims reviewer. A user has just submitted the following claim details:

    - Claim Type: {claim_type}
    - Claim Amount: ₹{amount}
    - Incident Description: {description}

    Please do the following:
    1. Provide a short, friendly summary of the claim in simple language so the user feels assured.
    2. Mention if any documents or next steps might usually be needed (in general terms).
    3. Conclude with a polite note encouraging the user to await further communication.

    Respond as if you are directly speaking to the user.
    """
    return call_openrouter(prompt)
