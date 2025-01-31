from flask import Blueprint, request, jsonify
from extensions import firebase_db

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/send', methods=['POST'])
def send_message():
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    message = data.get('message')
    
    try:
        # Push the message to Firebase Realtime Database
        firebase_db.child('messages').child(sender_id).child(receiver_id).push({
            "message": message,
            "timestamp": {".sv": "timestamp"}  # Firebase server timestamp
        })
        return jsonify({"message": "Message sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@chat_bp.route('/messages/<sender_id>/<receiver_id>', methods=['GET'])
def get_messages(sender_id, receiver_id):
    try:
        # Retrieve messages from Firebase Realtime Database
        messages = firebase_db.child('messages').child(sender_id).child(receiver_id).get()
        # Convert messages to a list of dictionaries
        messages_list = [msg.val() for msg in messages.each()]
        return jsonify(messages_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400