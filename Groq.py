from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

from httpx import stream
import requests 
import os

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
        print("Exiting...")
        return

    # Query the LLM 
    stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": chat_content,
        }
    ],
    model="mixtral-8x7b-32768",
    stream=True,
    )

    for chunk in stream:
        print(chunk.choices[0].delta.content, end="")


def models():

    api_key = os.environ.get("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/models"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    print(response.json())

def advanced_mode():

    # Api
    client = Groq(
        api_key = os.getenv("GROQ_API_KEY"),
    )

    # Input
    chat_content = input("Hi, I'm Groq. How may I help you today? ")
    print("Your input is:", chat_content)

    # Confirmation    
    if input("Do you want to continue? (yes/no): ").lower() != "yes":
        print("Exiting...")
        return

    # Query the LLM 
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": chat_content,
        }
    ],
    model="mixtral-8x7b-32768",
    )

    result = chat_completion.choices[0].message.content
    print(result)


def main():

    # Mode
    mode = input("What mode do you want to use? (Simple/Advanced/Models): ").lower()
    if mode == "simple":
        simple_mode()

    elif mode == "advanced":
        print("Work in Progress")
        raise NotImplementedError("Advanced mode is not yet implemented")

    elif mode == "models":
        models()

    else:
        raise ValueError("Invalid mode selected")


if __name__ == "__main__":
    main()
