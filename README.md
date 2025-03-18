# ANUS Project

This repository contains a clone of the ANUS (Autonomous Networked Utility System) framework from the original [nikmcfly/ANUS](https://github.com/nikmcfly/ANUS) repository.

## Installation Instructions

Follow these steps to install and run the ANUS project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ThomasE11/anus-project.git
   cd anus-project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package in development mode**:
   ```bash
   pip install -e .
   ```

5. **Set up your API keys**:
   Create a `.env` file in the project root directory:
   ```bash
   cp .env.example .env
   ```
   
   Then edit the `.env` file to add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   Replace `your_openai_api_key_here` with your actual OpenAI API key.

6. **Configuration**:
   The default configuration is in `config.yaml`. You don't need to modify this file if you've set up your `.env` file correctly, as it will read the API key from your environment variables.

## Usage

### Interactive Mode

The easiest way to use ANUS is through the interactive interface:

```bash
python interactive_anus.py
```

This will start an interactive prompt where you can enter tasks for ANUS to perform.

### Example Commands

Once the interactive interface is running, you can try commands like:

- `Calculate 257 * 89`
- `What is the capital of Japan?`
- `Generate a Python function to calculate Fibonacci numbers`
- `Summarize the following text: [paste text here]`

### Available Tools

The framework includes several tools:
- Calculator - For mathematical calculations
- Search - For information lookup
- Text - For text processing
- Code - For code generation

### Agent Modes

ANUS now features a hybrid agent system that can:
- Automatically determine if a task requires single or multi-agent processing
- Use specialized agents for complex tasks (researcher, planner, executor, critic)
- Adjust to task complexity

## Requirements

- Python 3.11 or higher
- OpenAI API key (required for all functionality)

## Note

This is a demonstration project. Some tools may require additional API keys to function properly.