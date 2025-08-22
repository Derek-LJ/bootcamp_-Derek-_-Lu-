import os
from dotenv import load_dotenv
from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parent.parent

def load_env():
    # construct path to .env file
    env_path = get_project_root().parent / '.env'
    
    # load .env file
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        print(f"Loaded .env file from: {env_path}")
    else:
        print(f"Warning: .env file not found at {env_path}")

def get_api_key():
    # gets API key from environment variables
    return os.getenv("API_KEY")