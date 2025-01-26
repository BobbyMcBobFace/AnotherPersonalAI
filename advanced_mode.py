from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os
from models import models

load_dotenv(dotenv_path=Path('.') / '.env')

def advanced_mode():
    # Api
    client = Groq(
        api_key = os.getenv("GROQ_API_KEY"),
    )

    # Input
    models()    
    selected_model = input("\nPlease select your chosen AI model. For more info, visit https://console.groq.com/docs/models: ")
    system_content = input("\nPlease set the system behaviour message: ")
    chat_content = input("\nHi, I'm Groq. How may I help you today? ")
    print("Your input is:", chat_content)
    print("Your selected model is:", selected_model)

    # Confirmation    
    if input("Do you want to continue? (yes/no): ").lower() != "yes":
        print("\nReturning to main menu...")
        return

    # Query the LLM 
    stream = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_content
        },
        {
            "role": "user",
            "content": chat_content,
        }
    ],  
    model=selected_model,
    stream=True,
    )

    for chunk in stream:
        print(chunk.choices[0].delta.content, end="")
