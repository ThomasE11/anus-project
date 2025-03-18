"""
Anus - Autonomous Networked Utility System
Main entry point for the Anus AI agent framework
"""

import argparse
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

from anus.core.orchestrator import AgentOrchestrator
from anus.ui.cli import CLI

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

def main():
    """Main entry point for the Anus AI agent"""
    # Load environment variables
    env_loaded = load_environment()
    
    parser = argparse.ArgumentParser(description="Anus AI - Autonomous Networked Utility System")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to configuration file")
    parser.add_argument("--mode", type=str, default="auto", choices=["single", "multi", "auto"], help="Agent mode")
    parser.add_argument("--task", type=str, help="Task description")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    
    # Initialize the CLI
    cli = CLI(verbose=args.verbose)
    
    # Display welcome message
    cli.display_welcome()
    
    # Check if OpenAI API key is available
    if not os.environ.get("OPENAI_API_KEY"):
        cli.display_error("OpenAI API key not found in environment variables or .env file.")
        cli.display_message("Please set your API key by either:")
        cli.display_message("1. Creating a .env file in the project root with OPENAI_API_KEY=your_key")
        cli.display_message("2. Setting the OPENAI_API_KEY environment variable directly")
        sys.exit(1)
    
    # Initialize the agent orchestrator
    orchestrator = AgentOrchestrator(config_path=args.config)
    
    # If task is provided as argument, execute it
    if args.task:
        result = orchestrator.execute_task(args.task, mode=args.mode)
        cli.display_result(result)
        return
    
    # Otherwise, start interactive mode
    cli.start_interactive_mode(orchestrator)

if __name__ == "__main__":
    main()