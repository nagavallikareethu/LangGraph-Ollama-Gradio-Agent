# LangGraph-Ollama-Gradio-Agent

# 🚀 LangGraph Ollama Gradio Agent

This project shows how to build and run an **AI Agent** using:
- **LangGraph** for agent workflows
- **Ollama** for local LLMs like Mistral, Llama2, or Gemma
- **Gradio** for a simple web user interface

---

## 📁 Folder Structure

langgraph_agent/
├── agent_graph.py
├── requirements.txt
├── README.md
└── .gitignore


---

## ✅ How to Use — **Full Process**

Follow these simple steps to set up, run, and deploy your agent.

---

## 1️⃣ **Clone this project**

First, clone your GitHub repo:


git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
cd <YOUR_REPO>
2️⃣ Create a virtual environment
Create and activate a Python virtual environment to keep your packages organized.


# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
3️⃣ Install dependencies
Install all required Python packages:


pip install -r requirements.txt
4️⃣ Pull and run Ollama models
Make sure Ollama is installed and running.
Start by pulling a model like mistral:


ollama pull mistral
ollama serve
ollama serve starts the Ollama server on localhost:11434 by default.

5️⃣ Run the Gradio Agent
Now launch your agent with:


python agent_graph.py
Gradio will start and show a local link like:
Running on http://127.0.0.1:7860
Open that link in your browser to test your agent!

6️⃣ Push to GitHub
When everything works, push your project:


git init
git add .
git commit -m "Initial commit: LangGraph Ollama Gradio Agent"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
git push -u origin main
✅ ✅ Optional: How It Works
agent_graph.py sets up:

OllamaLLM for your local model

LangGraph nodes to run prompts

Gradio as the user interface

When you type a question in Gradio:

It goes through the LangGraph

The graph calls Ollama for a reply

The answer shows in your browser!

