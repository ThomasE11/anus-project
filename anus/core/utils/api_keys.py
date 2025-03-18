"""
Utility functions for managing API keys in ANUS.
"""

import os
import sys
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

def load_environment() -> bool:
    """
    Load environment variables from .env file.
    
    Returns:
        bool: True if any .env file was found and loaded, False otherwise.
    """
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

def get_openai_api_key() -> Optional[str]:
    """
    Get the OpenAI API key from environment variables.
    
    Returns:
        Optional[str]: The API key if found, None otherwise.
    """
    # Try to load environment variables if not already loaded
    load_environment()
    
    # Get API key from environment variables
    return os.environ.get("OPENAI_API_KEY")

def validate_api_keys(required_keys: list = ["OPENAI_API_KEY"]) -> bool:
    """
    Validate that all required API keys are present.
    
    Args:
        required_keys: List of required API key environment variable names.
        
    Returns:
        bool: True if all required keys are present, False otherwise.
    """
    # Try to load environment variables if not already loaded
    load_environment()
    
    # Check each required key
    missing_keys = []
    for key in required_keys:
        if not os.environ.get(key):
            missing_keys.append(key)
    
    return len(missing_keys) == 0

def ensure_api_keys(required_keys: list = ["OPENAI_API_KEY"], exit_on_missing: bool = True) -> bool:
    """
    Ensure that all required API keys are present, with helpful error messages if not.
    
    Args:
        required_keys: List of required API key environment variable names.
        exit_on_missing: Whether to exit the program if keys are missing.
        
    Returns:
        bool: True if all required keys are present, False otherwise.
    """
    # Try to load environment variables if not already loaded
    load_environment()
    
    # Check each required key
    missing_keys = []
    for key in required_keys:
        if not os.environ.get(key):
            missing_keys.append(key)
    
    if missing_keys:
        print(f"\nError: The following API keys are missing: {', '.join(missing_keys)}")
        print("Please set these keys by either:")
        print("1. Creating a .env file in the project root with the required keys")
        print("2. Setting the environment variables directly")
        
        if exit_on_missing:
            sys.exit(1)
        return False
    
    return True