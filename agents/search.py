from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from tools.search_tool import search_tool

# Prompt template for the search agent
SEARCH_PROMPT = """
You are an expert researcher. Your task is to generate a list of 3-5 specific, targeted search queries to gather information for a blog post on the given topic and outline.
Only generate queries that are directly relevant to the provided outline sections.

Return the queries as a JSON object with a single key "queries" that contains a list of strings.

Topic: {topic}

Outline:
{outline}

JSON Response:
"""

def get_search_agent_runnable():
    # Returns the runnable for the search agent.

    prompt = ChatPromptTemplate.from_template(SEARCH_PROMPT)
    llm = ChatGroq(model="llama-3.3-70b-versatile")

    # Json parser to convert the LLM's output into Python List
    parser = JsonOutputParser()

    # Query generate chain using LCEL (Langchain Execution Language)
    query_generator = prompt | llm | parser

    return query_generator

def run_search_agent(topic: str, outline: str) -> list[dict]:
    """Runs the search agent to generate queries and execute them."""

    query_generator = get_search_agent_runnable()

    # 1. Generate list of search quried from LLM
    print("----- SEARCH AGENT: Generating search queries... -----")
    query_dict = query_generator.invoke({"topic" : topic, "outline": outline})
    queries = query_dict.get("queries", [])
    print(f"Generated Queries: {queries}")

    # 2.Run search tool for each query 
    research_data = []
    print("----- SEARCH AGENT: Running search tool... -----")
    for query in queries:
        try:
            print(f"Searching for: '{query}'")
            search_result = search_tool.invoke({"query": query})
            research_data.append({
                "query": query,
                "results": search_result
            })
        except Exception as e:
            print(f"Error searching for '{query}': {e}")
            research_data.append({
                "query": query,
                "results": f"Error occured: {e}"
            })

    return research_data

# Only for testing purpose
if __name__ == "__main__":
    sample_topic = "The Future of Renewable Energy"
    sample_outline = """
1. Introduction to Renewable Energy
2. Current Trends in Renewable Energy
3. Technological Innovations
4. Environmental and Economic Impacts
5. Future Prospects and Challenges
6. Conclusion
"""
    results = run_search_agent(sample_topic, sample_outline)
    print("=== Research Data (Search agent) ===")
    import json
    print(json.dumps(results, indent=2))