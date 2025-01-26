from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import sys
import os

load_dotenv(dotenv_path=Path('.') / '.env')

# Api
client = Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

def simple_mode():
    # Input
    chat_content = input("Hi, I'm Groq. How may I help you today? ")
    print("Your input is:", chat_content)

    # Confirmation    
    if input("Do you want to continue? (yes/no): ").lower() != "yes":
        print("\nReturning to main menu...")
        sys.exit()
    
    # Run the prompt through the guard first to ensure appropriate content
    guard_response = query_guard(chat_content)
    

    # If the message is safe, allow Llama to respond to it
    if guard_response.lower() == "safe":
        query_llm(chat_content)
    # If the message is unsafe, error out with a generic message 
    else:
        raise ValueError("Sorry, I cannot process this request due to inappropriate content.")
    

def query_guard(chat_content):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": chat_content
            }
        ],
        model="llama-guard-3-8b",
    )

    return chat_completion.choices[0].message.content


    
def query_llm(chat_content):
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


