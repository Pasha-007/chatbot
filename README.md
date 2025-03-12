# NLP Chatbot Project

## Overview
I built this chatbot application to strengthen my knowledge base for working with NLP, fastAPI etc.. 
It integrates OpenAI's GPT-4 API with a FastAPI backend and provides a clean, responsive chat interface.

The main goal was to demonstrate my ability to work with modern NLP technologies while showcasing API integration, backend development, and basic frontend skills.

## Features I Implemented

- Interactive real-time chat interface
- OpenAI GPT-4 integration for natural language understanding
- Asynchronous API handling with FastAPI
- Conversation context management
- Error handling for API limitations and failures
- Responsive frontend design

## Technologies Used

- **Backend**: Python, FastAPI, Uvicorn
- **NLP**: OpenAI GPT-4 API
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Ready for cloud deployment

## Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation

1. Clone this repository
```
git clone https://github.com/yourusername/chatbot-project.git
cd chatbot-project
```

2. Set up a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up your environment variables by creating a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Running the Application

Run the server with:
```
python -m app.main
```

Then open your browser to `http://localhost:8000`

## Project Structure

I organized the application with a clean separation of concerns:

- API routes are handled in the `routers` directory
- Business logic for OpenAI integration is in the `services` directory
- Frontend assets are stored in the `static` directory

## My Learning Process

Building this chatbot helped me better understand:
- How to structure a FastAPI application
- Techniques for managing API requests and responses
- The importance of error handling with external APIs
- How to maintain conversation context with LLMs

## Future Improvements

I plan to enhance this project with:
- PostgreSQL database for conversation persistence
- User authentication system
- More sophisticated prompt engineering
- Custom ML model to handle intent classification
- Docker containerization
- Monitoring for API usage and performance
