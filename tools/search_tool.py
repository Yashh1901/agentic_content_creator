# tools/search_tool.py

import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

if os.getenv("TAVILY_API_KEY") is None:
    raise ValueError("TAVILY_API_KEY not found in .env file. Please check your .env file.")

# Initialize Tavily search tool 
search_tool = TavilySearch(max_results=3)

# Testing purpose only
if __name__ == '__main__':
    print("Testing the search tool...")
    query = "What is LangGraph?"
    try:
        results = search_tool.invoke({"query": query})
        print("Search results:")
        print(results)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check if your TAVILY_API_KEY is correct in the .env file.")