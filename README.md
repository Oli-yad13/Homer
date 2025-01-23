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

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Oli-yad13/Homer.git
   ```

2. **Install dependencies:**

   ```bash
   pip install flask firebase-admin pymongo python-dotenv flask-cors
   ```

3. **Configure environment variables:**
   - Set your Firebase project credentials (download `firebase_credentials.json` and provide the path).
   - Configure your MongoDB connection details.

4. **Run the application:**

   ```bash
   flask run
   ```

## Contributing

Contributions are welcome! Please submit pull requests for bug fixes, feature enhancements, or improvements.

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, please contact [oliyadbekele.0@gmail.com].


