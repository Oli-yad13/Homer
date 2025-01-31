from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

# Define your routes here
@admin_bp.route('/')
def admin_home():
    return "Admin Home"