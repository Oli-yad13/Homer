from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

# Import routes at the end to avoid circular imports
from .routes import *