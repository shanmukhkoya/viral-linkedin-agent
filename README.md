# 🚀 Viral Topic Researcher & LinkedIn Post Generator

An **Agentic AI Application** that autonomously researches viral trends and generates professional LinkedIn posts using local Large Language Models (LLMs).

## 🤖 Why is this an "Agentic" Application?
Unlike a standard chatbot that just answers questions, this application is composed of specialized **AI Agents** that have specific roles, goals, and tools. They work together in a workflow to achieve a complex task:

### 1. 🕵️‍♂️ The Research Agent
*   **Role**: Information Gatherer & Analyst.
*   **Goal**: Find the most relevant and viral news topics.
*   **Tools**: `GoogleNewsSearch` (Custom tool using RSS feeds).
*   **Agentic Behavior**: It doesn't just "know" things; it actively **goes out to the web** (via RSS) to fetch real-time data from the last 72 hours, filters it, and summarizes it into a briefing document.

### 2. ✍️ The Content Agent
*   **Role**: Creative Writer & Social Media Strategist.
*   **Goal**: Craft engaging, high-impact content.
*   **Context**: It receives the "Briefing" from the Research Agent, not just raw data.
*   **Agentic Behavior**: It applies specific "Persona" instructions (Professional, Controversial, etc.) and formatting rules (Hooks, Emojis, Hashtags) to transform dry facts into engaging narratives.

---

## 🛠️ Detailed Tech Stack

### **Core Frameworks**
*   **[Python 3.10+](https://www.python.org/)**: The backbone programming language.
*   **[Streamlit](https://streamlit.io/)**: Used to build the interactive web UI and manage the agent orchestration/state.
*   **[LangChain](https://www.langchain.com/)**: The orchestration framework used to define the Agents, Prompts, and Chains.

### **AI & LLMs (Local)**
*   **[Ollama](https://ollama.com/)**: The local LLM runtime that allows us to run powerful models without cloud APIs.
*   **Models Supported**:
    *   `llama3`: High intelligence, great for complex reasoning.
    *   `phi3`: Balanced performance, low resource usage.
    *   `gemma2:2b`: Ultra-fast, optimized for laptops.

### **Tools & Utilities**
*   **`feedparser`**: A library to fetch and parse XML RSS feeds from Google News in real-time.
*   **`duckduckgo-search`**: (Optional) For fallback web searching.
*   **`BeautifulSoup`**: For cleaning and parsing HTML content from fetched articles.

### **DevOps & Deployment**
*   **Docker**: Containerized the application for consistent deployment.
*   **Docker Compose**: Orchestrates the App and Ollama services together.
*   **Git**: Version control.

---

## 🌟 Features
*   **Viral Topic Research**: Fetches the latest viral news from Google News RSS (last 3 days).
*   **AI Content Generation**: Uses local LLMs to write professional, engaging LinkedIn posts.
*   **Privacy First**: Runs entirely locally on your machine. No data is sent to the cloud.
*   **Performance Optimized**: Smart caching (`@st.cache_data`) and support for lightweight models (`gemma2:2b`).

## 📦 Installation (Plug & Play)

### 1. Clone the Repository
Open a terminal (Command Prompt or PowerShell) and run:
```powershell
git clone https://github.com/shanmukhkoya/viral-linkedin-agent.git
cd viral-linkedin-agent
```

### 2. Install Dependencies
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Setup Ollama
Make sure Ollama is installed. Then pull the models:
*   `ollama pull phi3` (Recommended)
*   `ollama pull gemma2:2b` (Fastest)

## 🚀 How to Run
**Option 1: Double-click `run.bat`** (Easiest)

**Option 2: Run via Terminal**
```powershell
.\run.bat
```
The application will open in your browser at `http://localhost:8501`.

## � Docker Deployment
```powershell
docker-compose up --build
```

## ❓ Troubleshooting
### "git is not recognized" Error
If you see this error after installing Git, try restarting your terminal.
In PowerShell, you can also use the full path:
```powershell
& "C:\Users\102139\AppData\Local\Programs\Git\cmd\git.exe" push -u origin main
```
