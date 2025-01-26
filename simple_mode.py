from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path('.') / '.env')

def simple_mode():
    # Api
    client = Groq(
        api_key = os.getenv("GROQ_API_KEY"),
    )

    # Input
    chat_content = input("Hi, I'm Groq. How may I help you today? ")
    print("Your input is:", chat_content)

    # Confirmation    
    if input("Do you want to continue? (yes/no): ").lower() != "yes":
        print("\nReturning to main menu...")
        return

    # Query the LLM 
    stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": chat_content,
        }
    ],
    model="llama-3.3-70b-versatile",
    stream=True,
    )

    for chunk in stream:
        print(chunk.choices[0].delta.content, end="")
