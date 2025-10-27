from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Prompt template for reviewer agent
REVIEWER_PROMPT = """
You are an expert editor and senior content reviewer. Your task is to review a blog post draft and decide if it is ready for publication or if it needs revision.

**Review Criteria:**
- **Clarity:** Is the language clear, concise, and easy to understand?
- **Accuracy:** Are the facts presented accurately based on the topic?
- **Structure:** Does the post follow a logical flow and is it well-organized?
- **Engagement:** Is the content engaging for the target audience?

**Your Decision:**
Based on your review, you must make a decision. Your output MUST be a JSON object with two keys:
1.  `"decision"`: A string that is either "approve" or "revise".
2.  `"feedback"`: A string providing detailed feedback. If the decision is "approve", this can be a simple "Looks good!". If "revise", provide specific, actionable feedback for the writer to improve the draft.

**Here is the content for your review:**

**Topic:**
{topic}

**Draft:**
{draft}

**JSON Response:**
"""

def get_reviewer_agent_runnable():
    # Returns runnable for the reviewer agent
    prompt = ChatPromptTemplate.from_template(REVIEWER_PROMPT)

    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature = 0)
    parser = JsonOutputParser()

    reviewer_agent_runnable = prompt | llm | parser

    return reviewer_agent_runnable

# Optional: Test block
if __name__ == '__main__':
    reviewer = get_reviewer_agent_runnable()
    
    # Sample data to test the reviewer
    sample_topic = "The Future of Renewable Energy"
    # A sample draft with some issues
    sample_draft = """
    Renewable energy is important. Solar panels use the sun. Wind turbines use the wind. 
    This is good for the earth. The future is green. Perovskite solar cells are new. 
    The end.
    """
    
    review = reviewer.invoke({
        "topic": sample_topic,
        "draft": sample_draft
    })
    
    print("----- REVIEWER AGENT DECISION -----")
    import json
    print(json.dumps(review, indent=2))

    # Test with a better draft
    better_draft = """
    ## The Dawn of a Greener Tomorrow: The Future of Renewable Energy
    As global imperatives shift towards sustainability, renewable energy stands at the forefront of our transition from fossil fuels. This move is driven by both environmental concerns and significant advancements in technology, making green energy more affordable and efficient than ever before.

    ### Key Technologies Leading the Charge
    - **Solar Power**: Innovations like perovskite solar cells and bifacial panels are revolutionizing efficiency, capturing more energy from the sun.
    - **Wind Power**: Offshore wind farms are becoming larger and more powerful, harnessing stronger, more consistent winds.
    
    While challenges in energy storage and grid integration remain, the trajectory is clear. Continuous innovation promises a future powered by clean, sustainable, and renewable resources.
    """
    review_good = reviewer.invoke({
        "topic": sample_topic,
        "draft": better_draft
    })

    print("\n----- REVIEWER AGENT DECISION (GOOD DRAFT) -----")
    print(json.dumps(review_good, indent=2))