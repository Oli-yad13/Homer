# Homer

A real-time chat application inspired by Instagram Direct Messaging.

## Features

- **User Registration & Login:** Firebase Authentication for secure signup/login.
- **Real-Time Messaging:** Firebase Firestore for instant message delivery.
- **Media Support:** Send images/videos (store URLs in MongoDB, files in Firebase Storage).
- **Analytics Dashboard:** Track user activity with MongoDB-aggregated data.
- **Admin Panel:** Manage users and messages (future enhancement).

## Technologies

- **Backend:** Python/Flask
- **Database:** MongoDB (user data, message history), Firebase Firestore (real-time sync)
- **Authentication:** Firebase Auth
- **Frontend:** HTML/CSS/JavaScript (basic templates for now)

## Setup Guide

### Prerequisites
- Python 3.9+
- MongoDB installed locally
- Firebase project with Firestore enabled

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Oli-yad13/Homer.git
   cd Homer
   python -m venv env

## Create a virtual environment:
    source env/bin/activate  # Linux/Mac
    .\env\Scripts\activate   # Windows

## Install dependencies:
    pip install flask firebase-admin pymongo python-dotenv flask-cors

## Configure environment variables:
   Create .env in the project root:
      ini
      Copy
      SECRET_KEY=your_flask_secret_key
      FIREBASE_CREDENTIALS=path/to/firebase-adminsdk.json
      MONGO_URI=mongodb://localhost:27017/homer_db
   Replace path/to/firebase-adminsdk.json with your actual Firebase service account path.


**Run the application:**

   ```bash
   flask run
   ```


## Contributing

Contributions are welcome! Please submit pull requests for bug fixes, feature enhancements, or improvements.

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, please contact [oliyadbekele.0@gmail.com].

  
