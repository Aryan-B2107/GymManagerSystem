# app.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from flask import Flask
from backend.config import Config
from backend.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    # Adding the configurations as settings for our flask app:
    app.config.from_object(config_class)

    # Initialise the db extension with the app
    db.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        # This is the crucial change: explicitly import the models module itself.
        import backend.models
        db.create_all()
    app.run(debug=True)
