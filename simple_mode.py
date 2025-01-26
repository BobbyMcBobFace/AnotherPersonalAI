import re
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path('.') / '.env')

# Api
client = Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

def simple_mode(chat_content=None, is_gui=False):
    """
    Simple mode function that works in both CLI and GUI
    
    Args:
        chat_content (str, optional): Prompt for processing
        is_gui (bool): Flag to indicate GUI or CLI mode
    
    Returns:
        str: Response or error message
    """
    try:
        # If no content provided, use CLI input
        if chat_content is None:
            chat_content = input("Hi, I'm Groq. How may I help you today? ")
            print("Your input is:", chat_content)

            # CLI Confirmation    
            if input("Do you want to continue? (yes/no): ").lower() != "yes":
                return None

        # Run the prompt through the guard first to ensure appropriate content
        guard_response = query_guard(chat_content)

        # If the message is safe, allow Llama to respond to it
        if guard_response == "safe":
            response = query_llm(chat_content)
            
            # Return differently based on mode
            if is_gui:
                return response
            else:
                print(response)
                print("\n")
                return response

        else:
            error_msg = "Sorry, I cannot process this request due to inappropriate content."
            
            # Return differently based on mode
            if is_gui:
                return error_msg
            else:
                raise ValueError(error_msg)

    except Exception as e:
        # Handle errors consistently
        if is_gui:
            return str(e)
        else:
            print(f"Error: {e}")
            return None

def query_guard(chat_content):
    """
    Check content safety using Llama Guard
    
    Args:
        chat_content (str): User prompt to check
    
    Returns:
        str: Safety status
    """
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
    """
    Query LLM and return full response
    
    Args:
        chat_content (str): User prompt
    
    Returns:
        str: Full LLM response
    """
    response = ""
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
        content = chunk.choices[0].delta.content
        if content:
            response += content
            # Optional: print for CLI mode
            print(content, end="")
    
    return response

# Remove returntomain() function as it's no longer needed
# Navigation will be handled in the GUI

# Allow direct script execution
if __name__ == "__main__":
    simple_mode()
