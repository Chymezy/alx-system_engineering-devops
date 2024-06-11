from datetime import datetime
from backend.utils.db import db


# Importance: Manages user energy consumption records.

class EnergyRecord(db.Model):
    # Define columns for energy record attributes
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    consumption = db.Column(db.Float, nullable=False)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define relationship to User model
    user = db.relationship('User', back_populates='energy_records')

