import os
from typing import List, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class OpenAIService:
    def __init__(self):
        # Initialize OpenAI client
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        
        self.client = OpenAI(api_key=self.api_key)
        
        # Load configuration from environment
        self.model_name = os.getenv("MODEL_NAME", "gpt-4")
        self.max_tokens = int(os.getenv("MAX_TOKENS", 150))
        self.temperature = float(os.getenv("TEMPERATURE", 0.7))
    
    async def get_chat_response(self, messages: List[Dict[str, str]]) -> str:
        """
        Get a response from the OpenAI API based on the conversation history.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
                     Example: [{"role": "user", "content": "Hello!"}]
        
        Returns:
            The assistant's response as a string
        """
        try:
            # Call the OpenAI API
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            # Extract and return the response text
            return response.choices[0].message.content
            
        except Exception as e:
            # Log the error (in a real application, use a proper logger)
            print(f"Error calling OpenAI API: {e}")
            
            # Return an error message
            return "I'm sorry, I encountered an error. Please try again later."

# Create a singleton instance
openai_service = OpenAIService()