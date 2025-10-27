Agentic Content Creator ✍️🤖

This project is an autonomous multi-agent system built using LangChain and LangGraph to automate the creation of high-quality blog posts.

You provide a single topic, and a team of AI agents collaborates to plan, research, write, and review a complete article, including a revision loop for quality assurance.

🚀 How It Works: The Agent Team

This system is built as a graph where each node is a specialized agent. The data (state) flows between them until a final, approved article is produced.

📝 Planner Agent:

Job: Acts as the Content Strategist.

Action: Takes the user's topic and creates a detailed, structured article outline.

🔎 Search Agent:

Job: Acts as the Research Analyst.

Action: Takes the outline, generates specific search queries for each section, and uses the Tavily API to gather real-time information from the web.

✍️ Writer Agent:

Job: Acts as the Content Writer.

Action: Receives the outline and the research data. Its task is to synthesize this information into a high-quality, coherent first draft.

🧐 Reviewer Agent:

Job: Acts as the Editor-in-Chief.

Action: Reads the draft and makes a critical decision:

approve: If the draft is high-quality and ready to be published.

revise: If the draft has issues, it provides specific feedback.

The Power of LangGraph: The Revision Loop 🔄

This is the most powerful feature of the project. The graph uses a conditional edge based on the Reviewer's decision:

If the decision is approve, the graph finishes and presents the final content.

If the decision is revise, the draft and the reviewer's feedback are sent back to the Writer Agent. The writer then improves the draft based on the feedback and resubmits it. This loop continues until the reviewer approves it or a maximum revision limit is hit.

🛠️ Tech Stack

Python 3.10+

LangGraph: For building the stateful, multi-agent workflow and cycles.

LangChain: For connecting components, managing prompts, and integrating with the LLM.

Groq: Provides the blazing-fast LLM inference (using models like meta-llama/llama-4-scout-17b-16e-instruct).

Tavily AI: For the smart search API.

🏁 How to Run This Project

1. Clone the Repository

git clone [https://github.com/your-username/agentic-content-creator.git](https://github.com/your-username/agentic-content-creator.git)
cd agentic-content-creator


2. Create and Activate a Virtual Environment

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate


3. Install Dependencies

All required libraries are listed in requirements.txt.

pip install -r requirements.txt


4. Set Up Your API Keys

You need API keys from Groq and Tavily.

Rename the .env.example file to .env.

Open the .env file and add your secret keys:

GROQ_API_KEY="gsk_YourGroqApiKeyHere"
TAVILY_API_KEY="tvly-YourTavilyApiKeyHere"


5. Run the Application!

Execute the main.py script. The program will prompt you to enter a topic.

python main.py


Example:

Please enter the blog post topic: The Impact of AI on Modern Art


Now, sit back and watch the agents collaborate in your terminal!

📂 Project Structure

/agentic_content_creator/
├── agents/               # Contains the logic for each agent
│   ├── planner.py
│   ├── search.py
│   ├── writer.py
│   └── reviewer.py
├── graph/                # Contains the LangGraph implementation
│   ├── state.py          # Defines the shared state (the "whiteboard")
│   └── builder.py        # Assembles the nodes and edges into the graph
├── tools/                # Contains external tools (e.g., search)
│   └── search_tool.py
├── .env                  # Stores secret API keys (ignored by Git)
├── .gitignore            # Tells Git which files to ignore
├── main.py               # The main entry point to run the project
├── requirements.txt      # List of Python dependencies
└── README.md             # You are here!
