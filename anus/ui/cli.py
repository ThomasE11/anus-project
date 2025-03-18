"""
Command-line interface for the ANUS framework.
"""

import sys
from typing import Dict, Any, Optional

class CLI:
    """
    Command-line interface for interacting with the ANUS framework.
    
    Provides a user-friendly interface for executing tasks and viewing results.
    """
    
    def __init__(self, verbose: bool = False):
        """
        Initialize a CLI instance.
        
        Args:
            verbose: Whether to enable verbose output.
        """
        self.verbose = verbose
    
    def display_welcome(self):
        """
        Display a welcome message when the CLI is started.
        """
        print("\n" + "="*50)
        print("ANUS - Autonomous Networked Utility System")
        print("="*50)
        print("Welcome to the ANUS command-line interface!")
        print("Type 'exit' or 'quit' to end the session.")
        print("="*50 + "\n")
    
    def display_result(self, result: Dict[str, Any]):
        """
        Display the result of a task execution.
        
        Args:
            result: The result of the task execution.
        """
        print("\nResult:")
        if isinstance(result, dict) and "answer" in result:
            print(result["answer"])
        else:
            print(result)
    
    def start_interactive_mode(self, orchestrator):
        """
        Start an interactive session with the agent orchestrator.
        
        Args:
            orchestrator: The agent orchestrator to use for executing tasks.
        """
        while True:
            try:
                # Get user input
                user_input = input("\nANUS> ")
                
                # Check for exit command
                if user_input.lower() in ["exit", "quit"]:
                    print("Exiting ANUS. Goodbye!")
                    break
                
                # Skip empty inputs
                if not user_input.strip():
                    continue
                
                # Process the task
                print("\nProcessing your request...\n")
                result = orchestrator.execute_task(user_input)
                
                # Display the result
                self.display_result(result)
                
            except KeyboardInterrupt:
                print("\nExiting ANUS. Goodbye!")
                break
            except Exception as e:
                print(f"\nError: {e}")
