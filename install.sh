#!/bin/bash

# ANUS Installation Script

echo -e "\n\033[1;36m=== ANUS - Autonomous Networked Utility System ===\033[0m"
echo -e "\033[1;36m=== Installation Script ===\033[0m\n"

# Check Python version
echo "Checking Python version..."
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
if [[ $(echo "$python_version >= 3.11" | bc -l) -eq 1 ]]; then
    echo -e "\033[0;32m✓ Python $python_version detected\033[0m"
else
    echo -e "\033[0;31m× Python 3.11 or higher is required, but $python_version was found\033[0m"
    echo "Please install Python 3.11 or higher and try again."
    exit 1
fi

# Create virtual environment
echo -e "\nCreating virtual environment..."
python3 -m venv venv
if [ $? -eq 0 ]; then
    echo -e "\033[0;32m✓ Virtual environment created\033[0m"
else
    echo -e "\033[0;31m× Failed to create virtual environment\033[0m"
    exit 1
fi

# Activate virtual environment
echo -e "\nActivating virtual environment..."
source venv/bin/activate
if [ $? -eq 0 ]; then
    echo -e "\033[0;32m✓ Virtual environment activated\033[0m"
else
    echo -e "\033[0;31m× Failed to activate virtual environment\033[0m"
    exit 1
fi

# Install dependencies
echo -e "\nInstalling dependencies..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo -e "\033[0;32m✓ Dependencies installed\033[0m"
else
    echo -e "\033[0;31m× Failed to install dependencies\033[0m"
    exit 1
fi

# Install package in development mode
echo -e "\nInstalling ANUS in development mode..."
pip install -e .
if [ $? -eq 0 ]; then
    echo -e "\033[0;32m✓ ANUS installed in development mode\033[0m"
else
    echo -e "\033[0;31m× Failed to install ANUS\033[0m"
    exit 1
fi

# Create configuration directory
echo -e "\nCreating configuration directory..."
mkdir -p ~/.anus
if [ $? -eq 0 ]; then
    echo -e "\033[0;32m✓ Configuration directory created\033[0m"
else
    echo -e "\033[0;31m× Failed to create configuration directory\033[0m"
    exit 1
fi

# Create configuration file
echo -e "\nCreating configuration file..."
if [ ! -f ~/.anus/config.yaml ]; then
    cat > ~/.anus/config.yaml << EOF
llm:
  provider: openai
  api_key: YOUR_OPENAI_API_KEY
  model: gpt-4o

# Agent settings
agent:
  verbose: true
  max_iterations: 10
  memory: 
    type: simple

# Tool settings
tools:
  browser:
    headless: true
  search:
    enabled: true
EOF
    echo -e "\033[0;32m✓ Configuration file created\033[0m"
    echo -e "\033[1;33m! Remember to edit ~/.anus/config.yaml and add your OpenAI API key\033[0m"
else
    echo -e "\033[0;33m! Configuration file already exists\033[0m"
fi

echo -e "\n\033[1;32m=== Installation Complete ===\033[0m"
echo -e "\nTo use ANUS, activate the virtual environment and run the interactive interface:"
echo -e "\n\033[1;36msource venv/bin/activate\033[0m"
echo -e "\033[1;36mpython interactive_anus.py\033[0m\n"