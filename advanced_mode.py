from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
from models import models
from main import main
import os


load_dotenv(dotenv_path=Path('.') / '.env')

# Api
client = Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

def advanced_mode():

    # Input
    models()    
    selected_model = input("\nPlease select your chosen AI model. For more info, visit https://console.groq.com/docs/models: ")
    system_content = input("\nPlease set the system behaviour message: ")
    chat_content = input("\nHi, I'm Groq. How may I help you today? ")
    print("Your input is:", chat_content)
    print("Your selected model is:", selected_model)

    # Confirmation
    if input("Do you want to continue? (yes/no): ").lower() != "yes":
        returntomain()

    guard_response = True if query_guard(chat_content) and query_guard(system_content) == "safe" else False

    # If the message is safe, allow selected model to respond to it
    if guard_response == True:
        query_llm(system_content, chat_content, selected_model)
        print("\n")
        returntomain()

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


def query_llm(system_content, chat_content, selected_model):
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

def returntomain():
    if input("Do you want to return to the main menu? (yes/no): ").lower() != "yes":
        advanced_mode()
    else:
        print("\nReturning to main menu...")
        main()
