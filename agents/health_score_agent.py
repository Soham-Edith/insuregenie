from utils.llm_utils import call_openrouter

def get_health_score_suggestions(has_term, has_health, has_critical, has_emergency_fund, recent_claims, score, language):
    prompt = f"""
    You are an expert insurance advisor. Please provide personalized, friendly, and actionable suggestions in {language}.

    User responses:
    - Has term plan: {"Yes" if has_term else "No"}
    - Has health insurance: {"Yes" if has_health else "No"}
    - Has critical illness cover: {"Yes" if has_critical else "No"}
    - Has emergency fund: {"Yes" if has_emergency_fund else "No"}
    - Recent major claims: {recent_claims}
    - Insurance health score: {score}/100

    Based on this, suggest practical improvements to increase their insurance readiness score. Keep it simple and motivating.
    """
    return call_openrouter(prompt)
