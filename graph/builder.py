import json
from langgraph.graph import StateGraph, END
from .state import AgentState
import time

from agents.planner import get_planner_agent_runnable
from agents.search import run_search_agent
from agents.writer import get_writer_agent_runnable
from agents.reviewer import get_reviewer_agent_runnable

MAX_REVISIONS = 1
# ____Node Definations_____

def planner_node(state: AgentState) -> dict:
    time.sleep(3)
    print("--- 📝 EXECUTING PLANNER ---")
    planner = get_planner_agent_runnable()
    outline = planner.invoke({"topic": state["topic"]})
    return {"outline": outline, "revision_number": 0}

def search_node(state: AgentState) -> dict:
    time.sleep(3)
    print("--- 🔎 EXECUTING RESEARCHER ---")
    research_data = run_search_agent(state["topic"], state["outline"])
    return {"research_data": research_data}

def writer_node(state: AgentState) -> dict:
    time.sleep(3)
    print("--- ✍️ EXECUTING WRITER ---")
    writer = get_writer_agent_runnable()
    formatted_research = json.dumps(state["research_data"], indent=2)
    draft = writer.invoke({
        "topic": state["topic"],
        "outline": state["outline"],
        "research_data": formatted_research,
        "feedback": state.get("feedback")   # Pass if exist
    })
    print(f"--- Draft:--- \n{draft}")
    revision_number = state.get("revision_number", 0) + 1
    return {"draft": draft, "revision_number": revision_number}

# In graph/builder.py

def reviewer_node(state: AgentState) -> dict:
    time.sleep(3)
    print("--- 🧐 EXECUTING REVIEWER ---")
    reviewer = get_reviewer_agent_runnable()
    review = reviewer.invoke({
        "topic": state['topic'],
        "draft": state['draft']
    })
    
    decision = review['decision']
    feedback = review['feedback']
    
    # Set final_content only if the decision is to approve
    if decision == 'approve':
        final_content = state['draft']
    else:
        final_content = None
        
    return {
        "decision": decision,
        "feedback": feedback,
        "final_content": final_content,
    }

# ______Conditional Edge Fucntion_________

def decide_to_finish(state: AgentState) -> str:

    """Conditional logic with a revision limit."""
    print("--- 🤔 CHECKING DECISION ---")

    # Check if the reviewer approved
    if state['decision'] == 'approve':
        print("--- ✅ DECISION: APPROVE ---")
        return "end"

    # Check if the revision limit has been reached
    elif state['revision_number'] > MAX_REVISIONS:
        print(f"--- ⚠️ MAX REVISIONS ({MAX_REVISIONS}) REACHED. FINISHING ---")
        # Set the final content to the last draft, even if not perfect
        state['final_content'] = state['draft']
        return "end"

    # Otherwise, send back for revision
    else:
        print("--- ❌ DECISION: REVISE ---")
        return "revise"
    
# _______Graph Assembly_________

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_node)
workflow.add_node("searcher", search_node)
workflow.add_node("writer", writer_node)
workflow.add_node("reviewer", reviewer_node)

# Set entry point of graph
workflow.set_entry_point("planner")

# Add edges to connect the nodes
workflow.add_edge("planner", "searcher")
workflow.add_edge("searcher", "writer")
workflow.add_edge("writer", "reviewer")

# add coditional edge for review loop
workflow.add_conditional_edges(
    "reviewer",
    decide_to_finish,
    {
        "revise": "writer",
        "end": END
    }
)

app = workflow.compile()
print("Workflow compiled successfully!")
