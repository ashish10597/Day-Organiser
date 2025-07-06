from langchain_openai import ChatOpenAI
from config import settings
from typing import Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from IPython.display import Image, display
import gradio as gr
from pydantic import BaseModel
import random

class State(BaseModel):
    messages: Annotated[list, add_messages]

class LLMClient:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=settings.OPENAI_API_KEY)
        self.graph = self._build_graph()
    
    def _build_graph(self):
        # Step 1: Start the Graph Builder with State class
        graph_builder = StateGraph(State)
        
        # Step 2: Create a Node
        def chatbot_node(old_state: State) -> State:
            response = self.llm.invoke(old_state.messages)
            new_state = State(messages=[response])
            return new_state
        
        graph_builder.add_node("chatbot", chatbot_node)
        
        # Step 3: Create Edges
        graph_builder.add_edge(START, "chatbot")
        graph_builder.add_edge("chatbot", END)
        
        # Step 4: Compile the Graph
        return graph_builder.compile()

    def get_response(self, prompt: str) -> str:
        # Create initial state with user message
        initial_state = State(messages=[{"role": "user", "content": prompt}])
        
        # Invoke the graph
        result = self.graph.invoke(initial_state)
        
        # Return the last message content
        return result['messages'][-1].content 