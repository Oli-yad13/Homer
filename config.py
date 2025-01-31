import os
from pathlib import Path
from dotenv import load_dotenv
from flask_cors import CORS

# Allow CORS for all routes
cors = CORS(resources={r"/auth/*": {"origins": "*"}})

# Load environment variables
load_dotenv()

class Config:
    # General Flask configuration
    SECRET_KEY = os.environ['SECRET_KEY']
    
    # Firebase Configuration
    FIREBASE_CREDENTIALS = Path(os.environ['FIREBASE_CREDENTIALS'])
    FIREBASE_DATABASE_URL = os.environ['FIREBASE_DATABASE_URL']
    
    # MongoDB Configuration
    MONGO_URI = os.environ['MONGO_URI']
    
    # Google Sign-In Configuration
    GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
    GOOGLE_CLIENT_SECRET = os.environ['GOOGLE_CLIENT_SECRET']