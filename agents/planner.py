from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser


# Prompt template for the planner
PLANNER_PROMPT = """
You are an expert content strategist and senior writer.
Your Task is to create a detailed, structured outline for a blog post on the given topic.
The outline should be comprehensive and cover all relevant subtopics and secions to create a high-quality, informative article.
Please provide the outline in a clear, easy-to-read text.

Topic: {topic}

Outline:
"""

def get_planner_agent_runnable():
    # returns the runnable for the planner agent.

    # Intialize the prompt template
    prompt = ChatPromptTemplate.from_template(PLANNER_PROMPT)

    # Initialize the language model with Groq
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature = 0)

    # Intialize Output Parser
    parser = StrOutputParser()

    # Create chain using LCEL (Langchain Execution Language)
    planner_agent_runnable = prompt | llm | parser

    return planner_agent_runnable

# Only for testing purpose
if __name__ == "__main__":
    planner = get_planner_agent_runnable()
    topic = "The Impact of Artificial Intelligence on Modern Healthcare"
    outline = planner.invoke({"topic": topic})
    print("=== Generated Outline (Planner agent) ===")
    print(outline)
