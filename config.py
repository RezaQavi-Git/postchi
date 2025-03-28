import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER_PORT = os.getenv("SERVER_PORT", 5000)
    