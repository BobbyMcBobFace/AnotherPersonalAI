import eel
from groq import Groq
from dotenv import load_dotenv
import os
import sys

# Import your existing modules
import simple_mode
import advanced_mode
import models

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initialize Eel
eel.init('web')

@eel.expose
def run_simple_mode(chat_content):
    """
    Run Simple Mode through Eel
    """
    try:
        response = simple_mode.simple_mode(chat_content, is_gui=True)
        return response
    except Exception as e:
        return f"Error in Simple Mode: {str(e)}"

@eel.expose
def run_advanced_mode(selected_model, system_content, chat_content):
    """
    Run Advanced Mode through Eel
    """
    try:
        response = advanced_mode.advanced_mode(
            selected_model, 
            system_content, 
            chat_content, 
            is_gui=True
        )
        return response
    except Exception as e:
        return f"Error in Advanced Mode: {str(e)}"

@eel.expose
def get_available_models():
    """
    Fetch available models
    """
    try:
        # Capture models output
        import io
        import sys
        
        old_stdout = sys.stdout
        result = io.StringIO()
        sys.stdout = result
        
        models.list_models()
        
        sys.stdout = old_stdout
        model_list = result.getvalue().split('\n')
        
        # Extract model IDs
        model_ids = [line.split('ID: ')[1].split(',')[0] for line in model_list if 'ID:' in line]
        
        return model_ids
    except Exception as e:
        return [f"Error fetching models: {str(e)}"]

def start_eel():
    """
    Start Eel application
    """
    eel.start('index.html', size=(1000, 800))


def return_to_main():
    # Logic to restart main menu
    start_eel()

if __name__ == "__main__":
    start_eel()
