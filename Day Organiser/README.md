# Day Organiser LLM Project

This project is a starter template for building LLM-powered applications using [LangGraph](https://github.com/langchain-ai/langgraph) and OpenAI, with future support for API exposure via FastAPI.

## Features

- Modular code structure for LLM interaction
- Environment variable management
- Ready for API integration (FastAPI)
- Virtual environment and dependency management

## Setup

1. **Clone the repository**
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r Day\ Organiser/requirements.txt
   ```
4. **Set up environment variables:**
   - Copy `.env.example` to `.env` and add your OpenAI API key:
     ```bash
     cp Day\ Organiser/.env.example Day\ Organiser/.env
     ```
   - Edit `.env` and set `OPENAI_API_KEY=your_openai_api_key_here`

## Usage

Run the CLI to test LLM responses:

```bash
python Day\ Organiser/main.py
```

## Project Structure

```
Day Organiser/
├── config.py         # Loads environment variables
├── llm_client.py     # LLM interaction logic (LangGraph + OpenAI)
├── main.py           # CLI for testing LLM
├── requirements.txt  # Python dependencies
├── .env.example      # Example environment variables
└── README.md         # Project documentation
```

## Next Steps

- Add FastAPI endpoints to expose LLM functionality to a frontend
- Expand LLM logic and prompt engineering
- Add tests and CI/CD
