from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

# Import routes at the end to avoid circular imports
from .routes import *