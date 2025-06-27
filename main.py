import streamlit as st
from agents.recommendation_agent import get_insurance_recommendation
from agents.claim_filing_agent import process_claim
from agents.fraud_detection_agent import analyze_fraud
from agents.policy_optimizer_agent import get_policy_comparison
from agents.chatbot_agent import generate_insurance_answer, explain_insurance_term
from agents.health_score_agent import get_health_score_suggestions
from agents.future_protection_agent import get_future_protection_plan



import pytesseract
from PIL import Image

# Point to your local Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.set_page_config(page_title="InsureGenie", layout="centered")
st.title("🧠 InsureGenie – Smart GenAI for Insurance")


st.sidebar.header("Choose a Service")
selected_agent = st.sidebar.radio("Agents", [
    "Insurance Product Recommendation",
    "Claim Filing Assistant",
    "Fraud Detection",
    "Customer Query Chatbot",
    "Policy Comparison & Optimizer",
    "Insurance Health Score",
    "Future Protection Plan"
])


if selected_agent == "Insurance Product Recommendation":
    st.subheader("📋 Insurance Product Recommendation")

    age = st.number_input("Enter your age", min_value=18, max_value=100, value=30)
    income = st.number_input("Enter your annual income (₹)", min_value=100000, step=50000, value=500000)
    goal = st.text_area("Describe your financial goal", placeholder="e.g., secure my family's future, retirement, child education...")

    if st.button("Get Recommendation"):
        with st.spinner("Analyzing your profile..."):
            output = get_insurance_recommendation(age, income, goal)
            st.success("Here are your personalized recommendations:")
            st.markdown(output)

elif selected_agent == "Claim Filing Assistant":
    st.subheader("📝 Claim Filing Assistant")

    claim_type = st.selectbox("Select claim type", ["Health", "Vehicle", "Life", "Property"])
    claim_amount = st.number_input("Enter claim amount (₹)", min_value=1000, step=5000, value=10000)
    incident_desc = st.text_area("Describe the incident", placeholder="e.g., My car was rear-ended on 5 June 2025 near Pune. No injuries, but rear bumper damaged.")

    st.markdown("💡 **Note:** Your claim amount does not need to exactly match the bill. It should reflect what you want to claim.")

    uploaded_file = st.file_uploader("Upload supporting document or image", type=["jpg", "jpeg", "png", "pdf"])

    extracted_text = ""
    if uploaded_file is not None:
        st.success("✅ File uploaded successfully!")
        if uploaded_file.type.startswith("image/"):
            st.image(uploaded_file, caption="Uploaded Image Preview", use_container_width=True)

            # OCR extraction
            img = Image.open(uploaded_file)
            extracted_text = pytesseract.image_to_string(img)

            st.markdown("### 📝 Extracted Text Preview")
            st.text(extracted_text.strip())

            # Check for health-related keywords
            if "hospital" in extracted_text.lower() or "medical" in extracted_text.lower():
                st.info("✔️ Health-related terms detected in the document.")
            else:
                st.warning("⚠️ No clear health-related keywords found in the document.")

            # Only show informational message about approximate amount
            if str(claim_amount)[:3] in extracted_text.replace(",", ""):
                st.info(f"ℹ️ Approximate entered amount ₹{claim_amount} appears in document (for your reference).")

        else:
            st.write("📄 Document uploaded (not displayed as an image). Please check manually.")

    if st.button("Submit Claim"):
        with st.spinner("Reviewing your claim details..."):
            summary = process_claim(claim_type, claim_amount, incident_desc)
            st.success("✅ Your claim has been reviewed and recorded!")
            st.markdown(summary)
            if uploaded_file:
                st.markdown("**📎 File was uploaded and previewed.**")
            else:
                st.markdown("⚠️ *No document was uploaded.*")

elif selected_agent == "Fraud Detection":
    st.subheader("🚨 Fraud Detection Agent")

    st.markdown("🔎 Describe your claim in detail. Our AI will analyze it for potential fraud risk.")

    fraud_desc = st.text_area("Describe your claim", placeholder="e.g., My bike was stolen last night from my society, but I don't have an FIR yet...")

    uploaded_file = st.file_uploader("Optional: Upload supporting document or image", type=["jpg", "jpeg", "png", "pdf"])

    if st.button("Analyze for Fraud"):
        with st.spinner("Analyzing for fraud risk..."):
            analysis = analyze_fraud(fraud_desc)
            st.success("✅ Analysis completed!")
            st.markdown(analysis)
            if uploaded_file:
                st.markdown("**📎 File was uploaded for reference.**")

elif selected_agent == "Policy Comparison & Optimizer":
    st.subheader("🧑‍🤝‍🧑 Policy Comparison & Optimizer Agent")

    budget = st.number_input("Enter your annual insurance budget (₹)", min_value=5000, step=5000, value=20000)
    goal = st.text_area("Describe your insurance goal", placeholder="e.g., Protect family financially after me, cover hospitalization expenses, etc.")

    st.markdown("💡 **Select your top priorities (you can choose multiple):**")
    priority_options = ["Family protection", "Health cover", "Critical illness cover", "Tax saving", "Low premium", "Comprehensive coverage"]
    selected_priorities = st.multiselect("Priorities", priority_options)

    if st.button("Get Optimized Recommendation"):
        with st.spinner("Analyzing and preparing comparison..."):
            comparison = get_policy_comparison(budget, goal, selected_priorities)
            st.success("✅ Here’s a personalized policy comparison for you:")
            st.markdown(comparison)


elif selected_agent == "Customer Query Chatbot":
    st.subheader("💬 Customer Query Chatbot")

    user_question = st.text_area("Ask me anything about insurance 👇", placeholder="e.g., What is a term plan? How to file a claim?")
    
    if st.button("Get Answer"):
        with st.spinner("Thinking..."):
            answer = generate_insurance_answer(user_question)
            st.success("Here's my answer:")
            st.markdown(answer)

    st.markdown("💡 **Want to quickly understand insurance terms? Let me explain them for you!**")

    terms_list = [
        "Premium", "Sum Assured", "No Claim Bonus", "Co-payment", "Rider", "Deductible",
        "Waiting Period", "Exclusions", "Grace Period", "Maturity Benefit",
        "Critical Illness Benefit", "Cashless Facility", "Underwriting", "Claim Settlement Ratio",
        "Portability", "Revival Period", "Surrender Value", "Free Look Period", "Top-up Plan"
    ]

    selected_term = st.selectbox("Select a term to get a detailed explanation:", ["Select"] + terms_list)

    if selected_term != "Select":
        if st.button("Get Term Explanation"):
            with st.spinner("Explaining..."):
                term_explanation = explain_insurance_term(selected_term)
                st.success(f"Here's an explanation for **{selected_term}**:")
                st.markdown(term_explanation)


elif selected_agent == "Insurance Health Score":
    st.subheader("🩺 My Insurance Health Score")

    st.markdown("💬 Answer a few quick questions to assess your insurance readiness score.")

    has_term = st.checkbox("I have a term insurance plan")
    has_health = st.checkbox("I have a health insurance policy")
    has_critical = st.checkbox("I have a critical illness rider or separate plan")
    has_emergency_fund = st.checkbox("I have an emergency fund or savings for 6+ months")
    recent_claims = st.radio("Have you made major claims in the last 3 years?", ["No", "Yes"])

    if st.button("Calculate My Score"):
        score = 50  # base score

        if has_term:
            score += 15
        if has_health:
            score += 15
        if has_critical:
            score += 10
        if has_emergency_fund:
            score += 10
        if recent_claims == "No":
            score += 10
        else:
            score -= 5  # small penalty for frequent claims

        # Cap score at 100
        score = min(score, 100)

        st.success(f"✅ Your Insurance Health Score: **{score}/100**")

        # Suggestions
        st.markdown("### 💡 Suggested Improvements")
        if not has_term:
            st.write("• Consider adding a term insurance plan for family protection.")
        if not has_health:
            st.write("• Consider getting a health insurance policy to cover medical costs.")
        if not has_critical:
            st.write("• Add a critical illness rider to protect against serious illnesses.")
        if not has_emergency_fund:
            st.write("• Build an emergency fund to handle unexpected events.")

        if score > 80:
            st.info("Great job! You are well-protected overall.")
        elif score > 60:
            st.info("You're on the right track, but there is room to improve.")
        else:
            st.warning("Your protection level is low. Consider taking action to improve your insurance readiness.")

elif selected_agent == "Insurance Health Score":
    st.subheader("🩺 My Insurance Health Score")

    st.markdown("💬 Answer a few quick questions to assess your insurance readiness score.")

    has_term = st.checkbox("I have a term insurance plan")
    has_health = st.checkbox("I have a health insurance policy")
    has_critical = st.checkbox("I have a critical illness rider or separate plan")
    has_emergency_fund = st.checkbox("I have an emergency fund or savings for 6+ months")
    recent_claims = st.radio("Have you made major claims in the last 3 years?", ["No", "Yes"])

    if st.button("Calculate My Score"):
        score = 50

        if has_term:
            score += 15
        if has_health:
            score += 15
        if has_critical:
            score += 10
        if has_emergency_fund:
            score += 10
        if recent_claims == "No":
            score += 10
        else:
            score -= 5

        score = min(score, 100)

        st.success(f"✅ Your Insurance Health Score: **{score}/100**")

        with st.spinner("Preparing personalized suggestions..."):
            suggestions = get_health_score_suggestions(has_term, has_health, has_critical, has_emergency_fund, recent_claims, score, "English")
            st.markdown("### 💡 Suggested Improvements")
            st.markdown(suggestions)

elif selected_agent == "Future Protection Plan":
    st.subheader("🔮 My Future Protection Plan")

    st.markdown("💬 Get a personalized step-by-step insurance + investment roadmap for the next 5–10 years.")

    age = st.number_input("Enter your age", min_value=18, max_value=65, value=25)
    income = st.number_input("Enter your annual income (₹)", min_value=100000, step=50000, value=500000)
    goal = st.text_area("Describe your major life/financial goals", placeholder="e.g., Secure family future, buy a home, retire early...")

    if st.button("Get My Plan"):
        with st.spinner("Preparing your future protection roadmap..."):
            plan = get_future_protection_plan(age, income, goal)
            st.success("✅ Here’s your personalized future protection plan:")
            st.markdown(plan)
