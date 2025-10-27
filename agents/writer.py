import json 
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Prompt template for writer agent
WRITER_PROMPT = """
You are an expert content writer, tasked with writing a high-quality, engaging, and well-structured blog post based on a given topic, outline, and research data.

Your goal is to synthesize the provided information into a coherent and informative article.

**Instructions:**
1.  **Follow the Outline:** Strictly adhere to the provided outline for the structure of the post.
2.  **Use the Research:** Base your writing on the provided research data. Do not include information that is not supported by the research.
3.  **Engaging Tone:** Write in a clear, concise, and engaging tone that is suitable for a blog post.
4.  **No Hallucinations:** Do not make up facts or information. Stick to the provided context.
5.  **Output Format:** Provide the complete blog post as a single block of text in Markdown format.

**Here is the context for your task:**

**Topic:**
{topic}

**Article Outline:**
{outline}

**Research Data:**
{research_data}

**Blog Post:**
"""

def get_writer_agent_runnable():
    # Returns runnable for the writer agent
    prompt = ChatPromptTemplate.from_template(WRITER_PROMPT)

    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature = 0.5)
    parser = StrOutputParser()

    writer_agent_runnable = prompt | llm | parser

    return writer_agent_runnable

# Optional: Test block
if __name__ == '__main__':
    writer = get_writer_agent_runnable()
    
    # Sample data to test the writer
    sample_topic = "The Future of Renewable Energy"
    sample_outline = """
    1. Introduction: The Shift to Sustainable Energy
    2. Key Types of Renewable Energy (Solar, Wind, Hydropower)
    3. Innovations and Future Trends
    4. Challenges and Obstacles
    5. Conclusion: A Greener Tomorrow
    """
    sample_research = [
        {'query': 'shift to sustainable energy', 'results': 'Global energy consumption is moving towards renewables due to climate change concerns and falling costs of solar and wind technologies.'},
        {'query': 'innovations in solar power', 'results': 'New developments include perovskite solar cells, which offer higher efficiency, and bifacial panels that capture light from both sides.'}
    ]
    
    # Convert research data to a string for the prompt
    formatted_research = json.dumps(sample_research, indent=2)
    
    draft = writer.invoke({
        "topic": sample_topic,
        "outline": sample_outline,
        "research_data": formatted_research
    })
    
    print("----- WRITER AGENT DRAFT -----")
    print(draft)
