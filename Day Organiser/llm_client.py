from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_core.runnables import RunnableLambda
from typing import TypedDict, Literal, Optional
from langchain_openai import ChatOpenAI
from config import settings

# -----------------------
# Define Shared State
# -----------------------
class AssistantState(TypedDict):
    user_input: str
    parsed_activity: Optional[dict]
    allocated_slots: Optional[list]
    reminders: Optional[list]
    feedback: Optional[str]

# -----------------------
# Node 1: Input Parser (LLM)
# -----------------------
def parse_input(state: AssistantState):
    # Use LLM to parse user input
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=settings.OPENAI_API_KEY)
    
    prompt = f"""
    Parse the following user input and extract activity information:
    User Input: {state['user_input']}
    
    Return a JSON object with:
    - title: Activity title
    - category: Activity category (work, learning, personal, etc.)
    - estimated_duration: Duration in minutes
    - constraints: Any time constraints (latest_time, min_block_size)
    - priority: Priority level (high, medium, low)
    
    Example format:
    {{
        "title": "Learn TypeScript",
        "category": "learning",
        "estimated_duration": 60,
        "constraints": {{
            "latest_time": "22:00",
            "min_block_size": 30
        }},
        "priority": "medium"
    }}
    """
    
    response = llm.invoke([{"role": "user", "content": prompt}])
    
    # Parse the response (in a real implementation, you'd use proper JSON parsing)
    # For now, returning a structured response
    parsed_activity = {
        "title": "Learn TypeScript",
        "category": "learning",
        "estimated_duration": 60,
        "constraints": {
            "latest_time": "22:00",
            "min_block_size": 30
        },
        "priority": "medium",
    }
    
    return {"parsed_activity": parsed_activity}

# -----------------------
# Node 2: Constraint Validator
# -----------------------
def validate_constraints(state: AssistantState):
    activity = state['parsed_activity']
    # Example: apply rules like "no time blocks after 10pm"
    # In reality, this would involve time logic and real-time calendar context
    valid = True
    if valid:
        return state
    else:
        raise Exception("Constraints not valid")

# -----------------------
# Node 3: Time Allocator
# -----------------------
def allocate_time_slots(state: AssistantState):
    activity = state['parsed_activity']
    # Simulate free time lookup in Postgres or calendar API
    allocated = [
        {"start": "2025-07-04T18:00", "end": "2025-07-04T19:00"},
        {"start": "2025-07-05T20:00", "end": "2025-07-05T21:00"},
    ]
    return {"allocated_slots": allocated}

# -----------------------
# Node 4: Calendar Updater
# -----------------------
def update_calendar(state: AssistantState):
    # Insert event into PostgreSQL or call Microsoft Graph API
    print("Updating calendar with:", state['allocated_slots'])
    return state

# -----------------------
# Node 5: Reminder Scheduler
# -----------------------
def schedule_reminders(state: AssistantState):
    # Simulate sending notifications (via Expo Push or cron jobs)
    reminders = [f"Reminder set for {slot['start']}" for slot in state['allocated_slots']]
    return {"reminders": reminders}

# -----------------------
# Node 6: Feedback Logger
# -----------------------
def log_feedback(state: AssistantState):
    # Save feedback in vector DB / Postgres
    print("Feedback logged for learning pattern...")
    return state

class LLMClient:
    def __init__(self):
        self.graph = self._build_graph()
    
    def _build_graph(self):
        # -----------------------
        # Graph Assembly
        # -----------------------
        workflow = StateGraph(AssistantState)
        workflow.add_node("ParseInput", RunnableLambda(parse_input))
        workflow.add_node("ValidateConstraints", RunnableLambda(validate_constraints))
        workflow.add_node("AllocateTime", RunnableLambda(allocate_time_slots))
        workflow.add_node("UpdateCalendar", RunnableLambda(update_calendar))
        workflow.add_node("ScheduleReminders", RunnableLambda(schedule_reminders))
        workflow.add_node("LogFeedback", RunnableLambda(log_feedback))

        # Define edges
        workflow.set_entry_point("ParseInput")
        workflow.add_edge("ParseInput", "ValidateConstraints")
        workflow.add_edge("ValidateConstraints", "AllocateTime")
        workflow.add_edge("AllocateTime", "UpdateCalendar")
        workflow.add_edge("UpdateCalendar", "ScheduleReminders")
        workflow.add_edge("ScheduleReminders", "LogFeedback")
        workflow.add_edge("LogFeedback", END)

        # Compile Graph
        return workflow.compile()

    def get_response(self, prompt: str) -> str:
        # Create initial state with user input
        initial_state = {"user_input": prompt}
        
        # Invoke the graph
        result = self.graph.invoke(initial_state)
        
        # Format the response
        response_parts = []
        
        if result.get('parsed_activity'):
            activity = result['parsed_activity']
            response_parts.append(f"✅ Activity parsed: {activity['title']} ({activity['category']})")
        
        if result.get('allocated_slots'):
            slots = result['allocated_slots']
            response_parts.append(f"📅 Time slots allocated: {len(slots)} slots")
            for i, slot in enumerate(slots, 1):
                response_parts.append(f"   {i}. {slot['start']} - {slot['end']}")
        
        if result.get('reminders'):
            reminders = result['reminders']
            response_parts.append(f"🔔 Reminders scheduled: {len(reminders)} reminders")
        
        response_parts.append("✅ Day organization complete!")
        
        return "\n".join(response_parts) 