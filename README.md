# 🤖 Agentic Content Creator ✍️

An autonomous multi-agent system built with LangChain and LangGraph to automate the creation of high-quality blog posts. Just provide a topic, and a team of AI agents will collaborate to plan, research, write, and review a complete article.

## ✨ Key Features

Autonomous Agent Team: A collaborative workforce of four specialized agents: Planner, Searcher, Writer, and Reviewer.

Self-Correcting Loop: Utilizes LangGraph's cyclical capabilities for automated revisions. If a draft isn't approved, it's sent back to the writer with actionable feedback, just like a real-world editorial team.

Real-Time Research: Integrates with the Tavily Search API to gather up-to-date information from the web.

Fast & Efficient: Built on Groq to leverage high-speed LLM inference, making the content generation process incredibly fast.

workflow-diagram

## 🛠️ Tech Stack

Python 3.10+

LangGraph: For building the stateful, multi-agent graph and cycles.

LangChain: For core agent components, prompts, and LLM integration.

Groq: For high-speed LLM inference (using meta-llama/llama-4-scout-17b-16e-instruct).

Tavily AI: For the intelligent web search API.

## 🏁 Getting Started

### 1. Set Up Your Environment

#### Clone the repository
git clone [https://github.com/Yashh1901/agentic_content_creator.git](https://github.com/Yashh1901/agentic_content_creator.git)
cd agentic-content-creator

#### Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate


### 2. Install Dependencies

pip install -r requirements.txt


### 3. Add API Keys

Create a .env file in the root directory and add your secret API keys:

GROQ_API_KEY="gsk_YourGroqApiKeyHere"
TAVILY_API_KEY="tvly-YourTavilyApiKeyHere"


### 4. Run the Application

python main.py


The application will prompt you to enter a topic. Just provide one and watch the agents work!

## 📂 Project Structure

/agentic_content_creator/

├── 📂 agents/           # Contains the logic for each agent

│   ├── planner.py

│   ├── search.py

│   ├── writer.py

│   └── reviewer.py

├── 📂 graph/           # LangGraph setup (State and Builder)

│   ├── state.py

│   └── builder.py

├── 📂 tools/           # External tools (e.g., search)

│   └── search_tool.py

├── 📄 .env             # Stores secret API keys (Git-ignored)

├── 📄 .gitignore       # Files for Git to ignore

├── 📄 main.py          # Main entry point to run the project

├── 📄 README.md        # You are here!

└── 📄 requirements.txt  # Python dependencies
