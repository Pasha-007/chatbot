from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import List, Dict, Optional
import os
from dotenv import load_dotenv

from app.services.openai_service import openai_service

# Load environment variables
load_dotenv()

# Create router
router = APIRouter(tags=["chat"])

# Models for request and response
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

class ChatResponse(BaseModel):
    response: str
    messages: List[Message]

# Simple in-memory conversation store
# In a real app, you'd use a database
conversations = {}

# API key verification (simple implementation)
async def verify_api_key(x_api_key: Optional[str] = Header(None)):
    # In development, you can disable this check
    # In production, implement proper authentication
    return True

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, _: bool = Depends(verify_api_key)):
    """
    Process a chat request and return a response from the AI.
    
    The request should contain a list of messages with roles ('user' or 'assistant')
    and content.
    """
    # Validate input
    if not request.messages:
        raise HTTPException(status_code=400, detail="No messages provided")
    
    # Format messages for OpenAI API and ensure valid roles
    messages = []
    for msg in request.messages:
        # Ensure role is one of the valid options
        if msg.role not in ["system", "assistant", "user", "function", "tool", "developer"]:
            # Default to "user" if invalid role
            role = "user"
        else:
            role = msg.role
        
        messages.append({"role": role, "content": msg.content})
    
    # Get response from OpenAI
    response_text = await openai_service.get_chat_response(messages)
    
    # Create assistant message
    assistant_message = Message(role="assistant", content=response_text)
    
    # Update conversation history
    updated_messages = request.messages + [assistant_message]
    
    # Return response
    return ChatResponse(
        response=response_text,
        messages=updated_messages
    )