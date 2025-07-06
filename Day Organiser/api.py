from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm_client import LLMClient
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Day Organiser LLM API",
    description="A REST API for LLM interactions using LangGraph and OpenAI",
    version="1.0.0"
)

# Initialize LLM client
llm_client = LLMClient()

# Request model
class PromptRequest(BaseModel):
    prompt: str

# Response model
class LLMResponse(BaseModel):
    response: str
    status: str = "success"

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Day Organiser LLM API is running!"}

@app.post("/api/chat", response_model=LLMResponse)
async def chat_with_llm(request: PromptRequest):
    """
    Send a prompt to the LLM and get a response
    
    Args:
        request: PromptRequest containing the user's prompt
        
    Returns:
        LLMResponse containing the LLM's response
    """
    try:
        response = llm_client.get_response(request.prompt)
        return LLMResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/api/health")
async def health_check():
    """Health check endpoint for the API"""
    return {"status": "healthy", "service": "Day Organiser LLM API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 