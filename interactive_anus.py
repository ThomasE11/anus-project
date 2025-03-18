from anus.core.agent.hybrid_agent import HybridAgent
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

def load_environment():
    """Load environment variables from .env file"""
    # Try to load from project root directory
    env_path = Path('.') / '.env'
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        return True
        
    # Try to load from parent directory if running from inside package
    env_path = Path('..') / '.env'
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        return True
        
    # Try to load from user's home directory
    env_path = Path.home() / '.anus' / '.env'
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        return True
        
    return False

def create_agent():
    """Create and configure an ANUS agent with available tools"""
    print("Initializing ANUS interface...")
    
    # Create a hybrid agent with multiple tools
    agent = HybridAgent(
        name="assistant",
        max_iterations=10,
        tools=["calculator", "search", "text", "code"]
    )
    
    return agent

def interactive_mode():
    """Run ANUS in interactive mode to accept user commands"""
    # Load environment variables
    env_loaded = load_environment()
    
    # Check if OpenAI API key is available
    if not os.environ.get("OPENAI_API_KEY"):
        print("\nError: OpenAI API key not found in environment variables or .env file.")
        print("Please set your API key by either:")
        print("1. Creating a .env file in the project root with OPENAI_API_KEY=your_key")
        print("2. Setting the OPENAI_API_KEY environment variable directly")
        sys.exit(1)
    
    agent = create_agent()
    
    # Print welcome message
    print("\n" + "="*50)
    print("ANUS - Autonomous Networked Utility System")
    print("Interactive Interface")
    print("="*50)
    print("Type 'exit' or 'quit' to end the session.")
    print("Type 'help' for assistance.")
    print("Enter your tasks and ANUS will process them.")
    print("="*50 + "\n")
    
    # Interactive loop
    while True:
        try:
            # Get user input
            user_input = input("\nANUS> ")
            
            # Check for exit command
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting ANUS interface. Goodbye!")
                break
                
            # Check for help command
            elif user_input.lower() == 'help':
                show_help()
                continue
            
            # Skip empty inputs
            if not user_input.strip():
                continue
                
            # Process the task
            print("\nProcessing your request...\n")
            result = agent.execute(user_input)
            
            # Display the result
            print("\nResult:")
            if isinstance(result, dict) and 'answer' in result:
                print(result['answer'])
            else:
                print(result)
                
        except KeyboardInterrupt:
            print("\nExiting ANUS interface. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")

def show_help():
    """Display help information"""
    print("\nANUS Interface Help:")
    print("  - Enter natural language tasks for ANUS to perform")
    print("  - Example tasks:")
    print("      * Calculate 257 * 89")
    print("      * What is the capital of Japan?")
    print("      * Generate a Python function to calculate Fibonacci numbers")
    print("      * Summarize the following text: [your text here]")
    print("  - Commands:")
    print("      * help  - Show this help message")
    print("      * exit  - Exit the interface")
    print("      * quit  - Exit the interface")

if __name__ == "__main__":
    interactive_mode()