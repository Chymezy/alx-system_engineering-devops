from datetime import datetime
from backend.utils.db import db


# Importance: Manages and stores analytics results.

class Analytics(db.Model):
    # Define columns for analytics attributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define relationship to User model
    user = db.relationship('User', back_populates='analytics')

