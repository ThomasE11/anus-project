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

5. **Create a configuration file**:
   ```bash
   mkdir -p ~/.anus
   ```

6. **Edit the configuration file**:
   Create a file at `~/.anus/config.yaml` with the following content:
   ```yaml
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
   ```
   
   Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

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

## Requirements

- Python 3.11 or higher
- OpenAI API key (for advanced functionality)

## Note

This is a demonstration project. Some tools may require additional API keys to function properly.