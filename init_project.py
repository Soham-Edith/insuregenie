import os

# Define folder structure
folders = [
    "agents",
    "utils",
    "pages"
]

files = {
    "main.py": "",
    ".env": "# Add your OpenAI API key like: OPENAI_API_KEY=sk-...\n",
    "requirements.txt": "streamlit\nopenai\nlangchain\npython-dotenv\n",
    "agents/__init__.py": "",
    "agents/recommendation_agent.py": "# Recommendation Agent logic\n",
    "agents/claim_filing_agent.py": "# Claim Filing Agent logic\n",
    "agents/fraud_detection_agent.py": "# Fraud Detection Agent logic\n",
    "agents/customer_query_agent.py": "# Customer Query Agent logic\n",
    "utils/__init__.py": "",
    "utils/llm_utils.py": "# LLM wrapper using OpenAI\n",
    "pages/placeholder.py": "# Placeholder for multi-page support in Streamlit\n"
}

def create_project_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for file_path, content in files.items():
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_project_structure()
