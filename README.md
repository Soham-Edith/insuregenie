# 🧠 InsureGenie – Smart GenAI for Insurance

## 🚀 Overview
**InsureGenie** is an AI-powered insurance advisory platform designed to guide users throughout their insurance journey. From personalized product recommendations to advanced future planning, InsureGenie provides a smart, friendly, and interactive experience.

---

## 💡 Key Features

- 📋 **Insurance Product Recommendation**  
  Get customized insurance product suggestions based on your age, income, and goals.

- 📝 **Claim Filing Assistant**  
  Helps you prepare and verify claims, with document OCR checks for better accuracy.

- 🚨 **Fraud Detection Agent**  
  Analyze your claim descriptions and detect potential fraud risks before submission.

- 💬 **Customer Query Chatbot**  
  Ask any insurance-related question and get clear, friendly answers instantly.

- 🧑‍🤝‍🧑 **Policy Comparison & Optimizer**  
  Compare policies based on budget and priorities to find the most optimized options.

- 🩺 **Insurance Health Score**  
  Evaluate your current insurance readiness score and receive actionable suggestions to improve it.

- 🔮 **Future Protection Plan**  
  Get a personalized step-by-step roadmap for the next 5–10 years covering insurance and investments. Perfect for young professionals!

---

## 🏗️ Architecture

- **Frontend**: Streamlit (for easy interactive UI).
- **Backend agents**: Python functions using dynamic LLM (Large Language Model) calls.
- **LLM integration**: OpenRouter API (or OpenAI, compatible).
- **OCR**: Tesseract (pytesseract) for claim document analysis.

---

## ⚙️ Setup Guide

### 🖥️ Local Setup

```bash
git clone https://github.com/yourusername/insure-genie.git
cd insure-genie
pip install -r requirements.txt
streamlit run main.py
