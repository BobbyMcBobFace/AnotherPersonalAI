from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

from httpx import stream
import requests 
import os
import json
import re

load_dotenv(dotenv_path=Path('.') / '.env')

# Simple mode - Only a prompt, nothing else 
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
        main()

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

def advanced_mode():

    # Api
    client = Groq(
        api_key = os.getenv("GROQ_API_KEY"),
    )

    # Input
    models()    
    selected_model = input("\nPlease select your chosen AI model. For more info, visit https://console.groq.com/docs/models: ")
    chat_content = input("\nHi, I'm Groq. How may I help you today? ")
    print("Your input is:", chat_content)
    print("Your selected model is:", selected_model)

    # Confirmation    
    if input("Do you want to continue? (yes/no): ").lower() != "yes":
        print("\nReturning to main menu...")
        main()

    # Query the LLM 
    stream = client.chat.completions.create(
    messages=[
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


def models():
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/models"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        # Regex match "id" and "owned_by" fields
        pattern = r'"id":\s*"([^"]*)".*?"owned_by":\s*"([^"]*)"'
        
        matches = re.findall(pattern, json.dumps(data), re.DOTALL)
        
        # Results
        print("Available models:")
        for id, owned_by in matches:
            print(f"ID: {id}, Owned by: {owned_by}")
    
    else:
        print(f"Error: {response.status_code} - {response.text}")

def main():

    # Mode
    mode = input("What mode do you want to use? (Simple/Advanced/Models/Exit): ").lower()
    if mode == "simple":
        simple_mode()

    elif mode == "advanced":
        advanced_mode()

    elif mode == "models":
        models()

    elif mode == "exit":
        raise ValueError("Exited!")

    else:
        raise ValueError("Invalid mode selected")


if __name__ == "__main__":
    main()
