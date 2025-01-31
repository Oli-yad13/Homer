from flask import Flask, render_template
from config import Config  # <-- Ensure Config is imported
from extensions import cors, mongo, firebase_db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    cors.init_app(app)
    mongo.init_app(app)
    
    # Register blueprints
    from auth.routes import auth_bp
    from chat.routes import chat_bp
    from admin.routes import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(chat_bp, url_prefix='/chat')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # Make Config available to all templates
    @app.context_processor
    def inject_config():
        return dict(Config=Config)  # <-- Add this context processor
    
    # Frontend routes
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/register')
    def register():
        return render_template('register.html')
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)