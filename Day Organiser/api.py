from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm_client import LLMClient
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Day Organiser LLM API",
    description="A REST API for intelligent day organization using LangGraph and OpenAI",
    version="1.0.0"
)

# Initialize LLM client
llm_client = LLMClient()

# Request model
class ActivityRequest(BaseModel):
    activity: str

# Response model
class OrganizationResponse(BaseModel):
    response: str
    status: str = "success"

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Day Organiser LLM API is running!"}

@app.post("/api/organize", response_model=OrganizationResponse)
async def organize_activity(request: ActivityRequest):
    """
    Organize an activity by parsing, validating, and scheduling it
    
    Args:
        request: ActivityRequest containing the activity description
        
    Returns:
        OrganizationResponse containing the organization results
    """
    try:
        response = llm_client.get_response(request.activity)
        return OrganizationResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error organizing activity: {str(e)}")

@app.get("/api/health")
async def health_check():
    """Health check endpoint for the API"""
    return {"status": "healthy", "service": "Day Organiser LLM API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 