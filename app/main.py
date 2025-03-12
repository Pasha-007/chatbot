import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.routers import chat

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="NLP Chatbot API",
    description="A simple chatbot API using OpenAI's GPT-4",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(chat.router, prefix="/api")

# Root endpoint - serve the index.html file
from fastapi.responses import FileResponse
import os

@app.get("/")
async def root():
    return FileResponse("app/static/index.html")

# Main entry point
if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    
    uvicorn.run("app.main:app", host=host, port=port, reload=True)