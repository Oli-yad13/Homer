from flask import Blueprint

chat_bp = Blueprint('chat', __name__)

# Import routes at the end to avoid circular imports
from .routes import *