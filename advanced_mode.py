from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os
import sys

load_dotenv(dotenv_path=Path('.') / '.env')

# Api
client = Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

def advanced_mode(selected_model=None, system_content=None, chat_content=None, is_gui=False):
    """
    Advanced mode function that works in both CLI and GUI
    
    Args:
        selected_model (str, optional): AI model to use
        system_content (str, optional): System behavior message
        chat_content (str, optional): User prompt
        is_gui (bool): Flag to indicate GUI or CLI mode
    
    Returns:
        str: Response or error message
    """
    try:
        # If no content provided, use CLI input
        if selected_model is None:
            from models import models
            models()    
            selected_model = input("\nPlease select your chosen AI model. For more info, visit https://console.groq.com/docs/models: ")
        
        if system_content is None:
            system_content = input("\nPlease set the system behaviour message: ")
        
        if chat_content is None:
            chat_content = input("\nHi, I'm Groq. How may I help you today? ")
            print("Your input is:", chat_content)
            print("Your selected model is:", selected_model)

            # CLI Confirmation    
            if input("Do you want to continue? (yes/no): ").lower() != "yes":
                return None

        # Run the prompt through the guard first to ensure appropriate content
        guard_response_content = query_guard(chat_content)
        guard_response_system = query_guard(system_content)

        # If both messages are safe, allow selected model to respond
        if guard_response_content == "safe" and guard_response_system == "safe":
            response = query_llm(system_content, chat_content, selected_model)
            
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
        chat_content (str): Content to check
    
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

def query_llm(system_content, chat_content, selected_model):
    """
    Query LLM and return full response
    
    Args:
        system_content (str): System behavior message
        chat_content (str): User prompt
        selected_model (str): AI model to use
    
    Returns:
        str: Full LLM response
    """
    response = ""
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
    advanced_mode()
