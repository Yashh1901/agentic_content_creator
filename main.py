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
    for event in app.stream(initial_state, stream_mode="values"):
        # The 'event' contains the current state of the workflow
        pass
    final_state = event

    print("\n--- ✅ WORKFLOW COMPLETE ---")
    print("\nHere is the final approved blog post:")
    print("-" * 50)
    print(final_state.get("final_content", "No content generated."))
    print("-" * 50)

if __name__ == "__main__":
    main()