import os
import requests
import json
import re
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path('.') / '.env')

def list_models():  # Change from models() to list_models()
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
