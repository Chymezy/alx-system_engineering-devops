from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from backend.utils.db import db

# Importance: Manages user data and authentication processes.
# class User(db.Model):
    # Define columns for user attributes
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define methods for password hashing and verification
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

