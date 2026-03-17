import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("OPENAI_API_KEY não definida nas variáveis de ambiente.")

OUTPUT_DIR = "output"
PROMPTS_DIR = "prompts"
