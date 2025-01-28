import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename='assistant.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_env_variable(var_name):
    value = os.getenv(var_name)
    if not value:
        raise Exception(f"Environment variable {var_name} is not set.")
    return value
