from flask import Flask
from app.routes import main
import os
from config import Config

def create_app():
    app = Flask(__name__)

    app.secret_key = Config.SECRET_KEY
    
    app.register_blueprint(main)

    return app
