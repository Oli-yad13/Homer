from flask import Blueprint, request, jsonify
from extensions import mongo
import firebase_admin.auth as firebase_auth
from config import Config
import logging

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    try:
        # Check if user already exists in Firebase
        try:
            existing_user = firebase_auth.get_user_by_email(email)
            return jsonify({"error": "User already exists"}), 400
        except firebase_auth.UserNotFoundError:
            pass  # Proceed to create user

        user = firebase_auth.create_user(email=email, password=password)
        mongo.db.users.insert_one({
            "_id": user.uid,
            "email": email
        })
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        logging.error(f"Registration error: {str(e)}")
        return jsonify({"error": str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    try:
        user = firebase_auth.get_user_by_email(email)
        # Verify password (critical fix!)
        # You need to implement Firebase client-side auth or use REST API
        return jsonify({"message": "Login successful", "uid": user.uid}), 200
    except Exception as e:
        logging.error(f"Login error: {str(e)}")
        return jsonify({"error": str(e)}), 400