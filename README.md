🤖 Agentic Content Creator ✍️Ek autonomous multi-agent system jo LangChain aur LangGraph ka istemal karke blog post create karne ke process ko automate karta hai. Aap sirf ek topic dein, aur AI agents ki ek team us par plan, research, write aur review karke ek complete article taiyaar kar degi.✨ Key FeaturesAutonomous Team: Chaar specialized agents (Planner, Searcher, Writer, Reviewer) ki ek team.Self-Correcting Loop: LangGraph ke cycles ka istemal karke automated revision. Agar draft achha nahi hai, to use feedback ke saath wapas writer ke paas bheja jaata hai, bilkul ek real-world team ki tarah.Real-Time Research: Tavily API ke saath integrate karke web se up-to-date information nikalta hai.Fast & Scalable: Groq par banaya gaya hai taaki LLM inference blazing-fast ho.🛠️ Tech StackPython 3.10+LangGraph: Stateful, multi-agent graph banane ke liye.LangChain: Core agent components aur prompts ke liye.Groq: High-speed LLM inference ke liye (using meta-llama/llama-4-scout-17b-16e-instruct).Tavily AI: Intelligent search API ke liye.🏁 Get Started (How to Run)1. Setup Your Environment# Repository ko clone karein
git clone [https://github.com/your-username/agentic-content-creator.git](https://github.com/your-username/agentic-content-creator.git)
cd agentic-content-creator

# Virtual environment banayein aur activate karein
python -m venv venv
source venv/bin/activate  # Windows par: .\venv\Scripts\activate

2. Install Dependenciespip install -r requirements.txt

3. Add API Keys.env naam ki ek file banayein aur usme apni API keys daalein:GROQ_API_KEY="gsk_YourGroqApiKeyHere"
TAVILY_API_KEY="tvly-YourTavilyApiKeyHere"

4. Run the Applicationpython main.py

Aapko ek topic enter karne ke liye kaha jayega. Bas topic dein aur agents ko kaam karte hue dekhein!📂 Project Structure/agentic_content_creator/
├── 📂 agents/          # Har agent ka logic (Planner, Searcher, etc.)
├── 📂 graph/           # LangGraph ka setup (State aur Builder)
├── 📂 tools/           # External tools (Search)
├── 📄 .env             # Secret API keys
├── 📄 .gitignore       # Woh files jo Git ko ignore karni hain
├── 📄 main.py          # Project ko run karne ki main file
├── 📄 README.md        # Aap yahan hain!
└── 📄 requirements.txt  # Zaroori Python libraries

