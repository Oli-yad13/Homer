from flask_cors import CORS
from flask_pymongo import PyMongo
import firebase_admin
from firebase_admin import credentials, db
from config import Config

# Initialize Flask extensions
cors = CORS()
mongo = PyMongo()

# Initialize Firebase
try:
    cred = credentials.Certificate(str(Config.FIREBASE_CREDENTIALS))
    firebase_app = firebase_admin.initialize_app(cred, {
        'databaseURL': Config.FIREBASE_DATABASE_URL
    })
    firebase_db = db.reference("/")  # Use reference() instead of ref
except Exception as e:
    print(f"🔥 Firebase initialization error: {e}")
    raise