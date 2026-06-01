# chatbot-ai

A lightweight Python chatbot powered by the OpenAI API. Supports both one-shot prompts and interactive terminal conversations.

## Features

- One-shot prompt mode via CLI flag
- Interactive REPL mode (run without a prompt flag)
- Configurable model, temperature, and system prompt
- API key loaded from a `.env` file or passed directly as a flag

## Requirements

- Python 3.8+
- An OpenAI API key

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chatbot-ai.git
   cd chatbot-ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy the env template and add your key:
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and replace `your-openai-api-key-here` with your actual key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys).

## Usage

**One-shot prompt:**
```bash
python chatbot_class.py --prompt "What is the capital of France?"
```

**With a system message:**
```bash
python chatbot_class.py --prompt "Explain recursion" --system "You are a patient teacher."
```

**Interactive mode:**
```bash
python chatbot_class.py
```

**All options:**
```
-p, --prompt       Question or prompt to send
-s, --system       Optional system prompt
-m, --model        Model name (default: gpt-4o-mini)
-t, --temperature  Sampling temperature (default: 0.7)
-k, --api-key      OpenAI API key (overrides .env)
```

## Project Structure

```
chatbot-ai/
├── chatbot_class.py   # ChatBot class and CLI entry point
├── requirements.txt   # Python dependencies
├── .env.example       # Template for required environment variables
├── .env               # Your API key — never committed to git
└── README.md
```
