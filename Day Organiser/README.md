# Day Organiser LLM Project

This project is an intelligent day organization system using [LangGraph](https://github.com/langchain-ai/langgraph) and OpenAI, with a FastAPI backend for activity scheduling and management.

## Features

- **Intelligent Activity Parsing**: Uses LLM to understand and parse user activities
- **Constraint Validation**: Validates time constraints and scheduling rules
- **Time Slot Allocation**: Automatically finds and allocates available time slots
- **Calendar Integration**: Updates calendar with scheduled activities
- **Reminder Scheduling**: Sets up notifications for scheduled activities
- **Feedback Logging**: Tracks user patterns for continuous improvement
- **REST API**: Ready for frontend integration
- **Modular Architecture**: Built with LangGraph for complex workflows

## Workflow

1. **Input Parser**: LLM parses user activity description
2. **Constraint Validator**: Validates scheduling constraints
3. **Time Allocator**: Finds available time slots
4. **Calendar Updater**: Updates calendar with events
5. **Reminder Scheduler**: Sets up notifications
6. **Feedback Logger**: Logs patterns for improvement

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

### CLI Testing

Test the day organization workflow:

```bash
python Day\ Organiser/main.py
```

### API Testing

Test the REST API:

```bash
python Day\ Organiser/test_api.py
```

### Direct Testing

Test the LLM client directly:

```bash
python Day\ Organiser/test_llm.py
```

## API Endpoints

### POST `/api/organize`

Organize an activity by parsing, validating, and scheduling it.

**Request:**

```json
{
  "activity": "I want to learn TypeScript for 2 hours tomorrow"
}
```

**Response:**

```json
{
  "response": "✅ Activity parsed: Learn TypeScript (learning)\n📅 Time slots allocated: 2 slots\n  1. 2025-07-04T18:00 - 2025-07-04T19:00\n  2. 2025-07-05T20:00 - 2025-07-05T21:00\n🔔 Reminders scheduled: 2 reminders\n✅ Day organization complete!",
  "status": "success"
}
```

### GET `/api/health`

Health check endpoint.

## Project Structure

```
Day Organiser/
├── config.py         # Loads environment variables
├── llm_client.py     # LangGraph workflow for day organization
├── api.py            # FastAPI REST API
├── main.py           # CLI for testing
├── requirements.txt  # Python dependencies
├── test_api.py       # API testing script
├── test_llm.py       # LLM testing script
├── .env.example      # Example environment variables
└── README.md         # Project documentation
```

## LangGraph Workflow

The system uses a 6-node LangGraph workflow:

1. **ParseInput**: LLM parses user activity description
2. **ValidateConstraints**: Validates scheduling constraints
3. **AllocateTime**: Finds available time slots
4. **UpdateCalendar**: Updates calendar with events
5. **ScheduleReminders**: Sets up notifications
6. **LogFeedback**: Logs patterns for improvement

## Next Steps

- Add real calendar integration (Google Calendar, Outlook)
- Implement database storage for activities and patterns
- Add user authentication and profiles
- Create frontend interface
- Add more sophisticated time allocation algorithms
- Implement real-time notifications

## Technologies Used

- **LangGraph**: Workflow orchestration
- **OpenAI GPT-4o-mini**: Natural language processing
- **FastAPI**: REST API framework
- **Pydantic**: Data validation
- **Uvicorn**: ASGI server
