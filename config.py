import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "random secret")
    SERVER_PORT = os.getenv("SERVER_PORT", 5000)
    