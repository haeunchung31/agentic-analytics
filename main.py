import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Agentic Analytics Orchestrator")
    parser.add_argument('query', nargs='?', help="The business question or analysis task")
    parser.add_argument('--mode', choices=['plan', 'execute', 'review'], default='plan', help="Execution mode")
    
    args = parser.parse_args()
    
    if not args.query:
        print("Welcome to Agentic Analytics. Please provide a query or task.")
        sys.exit(0)

    print(f"Received Query: {args.query}")
    print(f"Mode: {args.mode}")
    print("\nInitializing Agents...")
    # TODO: Initialize agents
    
    print("\nThinking...")
    # TODO: Orchestrate agent workflow
    
    print("\nDone.")

if __name__ == "__main__":
    main()
