# 🚀 Viral Topic Researcher & LinkedIn Post Generator

An AI-powered agentic application that searches the latest viral trends using Google News RSS and generates engaging LinkedIn posts using local LLMs (Ollama).

## 🌟 Features
*   **Viral Topic Research**: Fetches the latest viral news from Google News RSS (last 3 days).
*   **AI Content Generation**: Uses local LLMs (Llama 3, Phi-3, Gemma 2, Mistral) to write professional, engaging LinkedIn posts.
*   **Privacy First**: Runs entirely locally on your machine. No data is sent to the cloud.
*   **Performance Optimized**: 
    *   **Caching**: Smart caching ensures instant results for repeated queries.
    *   **Multiple Models**: Support for lightweight models (Phi-3, Gemma 2) for fast performance on laptops.
*   **Docker Ready**: Includes `Dockerfile` and `docker-compose.yml` for containerized deployment.

## 🛠️ Prerequisites
1.  **Python 3.10+**: [Download Here](https://www.python.org/downloads/)
2.  **Ollama**: [Download Here](https://ollama.com/download)
3.  **Git**: [Download Here](https://git-scm.com/downloads)

## 📦 Installation (Plug & Play)

### 1. Clone the Repository
Open a terminal (Command Prompt or PowerShell) and run:
```powershell
git clone https://github.com/<YOUR-USERNAME>/viral-research-agent.git
cd viral-research-agent
```

### 2. Install Dependencies
We have included a `requirements.txt` file with all necessary libraries.
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Setup Ollama (The AI Brain)
Make sure Ollama is installed and running. Then, pull the AI models you want to use.
*   **Recommended (Balanced):** `ollama pull phi3`
*   **Fastest (Laptop Friendly):** `ollama pull gemma2:2b`
*   **Most Powerful:** `ollama pull llama3`

## 🚀 How to Run
We have included a simple "One-Click" script to start the application.

**Option 1: Double-click `run.bat`**
Just find the `run.bat` file in the folder and double-click it!

**Option 2: Run via Terminal**
```powershell
.\run.bat
```

The application will open in your browser at `http://localhost:8501`.

## 💡 How to Use
1.  **Select Model**: In the sidebar, choose "phi3" or "gemma2:2b" for speed.
2.  **Select Tone**: Choose the tone for your post (Professional, Casual, etc.).
3.  **Enter Topic**: Type a topic like "Generative AI", "Data Science", or "Tech Layoffs".
4.  **Click Go**: Hit "Research & Generate Post".
5.  **Copy**: Read the research summary and copy the generated LinkedIn post!

## 🐳 Docker Deployment (Optional)
If you prefer running in a container:
```powershell
docker-compose up --build
```
*Note: This requires a powerful machine with 4GB+ RAM allocated to Docker.*

## 📂 Project Structure
*   `src/app.py`: Main Streamlit application.
*   `src/research_agent.py`: Agent that searches Google News.
*   `src/content_agent.py`: Agent that writes the posts.
*   `src/news_search_tool.py`: Tool for fetching RSS feeds.
*   `requirements.txt`: List of Python libraries.
