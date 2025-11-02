import cohere
import os
from dotenv import load_dotenv

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(COHERE_API_KEY)

def get_cohere_response(query: str) -> str:
    try:
        response = co.chat(
            model="command-r7b-12-2024",  # ✅ new model name
            message=query
        )
        return response.text
    except Exception as e:
        return f"Cohere API Error: {str(e)}"
