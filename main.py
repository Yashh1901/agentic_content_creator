from dotenv import load_dotenv
from graph.builder import app

load_dotenv()

def main():
    """Main function to run the agentic content creator."""

    # Get topic from user
    topic = input("Please enter the blog post topic: ")

    # Initial state with user-provided topic
    initial_state = {
        "topic": topic,
    }

    # Stream event from the graph
    print("--- 🚀 STARTING WORKFLOW ---")
    final_state = None
    
    for event in app.stream(initial_state, stream_mode="values"):
        # The 'event' contains the current state of the workflow
        final_state = event # Update final_state with every step
    
    print("\n--- ✅ WORKFLOW COMPLETE ---")
    print("\nHere is the final approved blog post:")
    print("-" * 50)
    
    # --- YAHAN CHANGE KIYA HAI ---
    # Pehle 'final_content' check karega, agar wo khali hai toh 'draft' utha lega
    content_to_print = final_state.get("final_content") or final_state.get("draft")
    
    if content_to_print:
        print(content_to_print)
    else:
        print("Error: No content generated.")
    # -----------------------------
    
    print("-" * 50)

if __name__ == "__main__":
    main()