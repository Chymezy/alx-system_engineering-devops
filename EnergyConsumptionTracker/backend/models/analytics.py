from backend.utils.db import db
from datetime import datetime

class Analytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_energy_consumed = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Analytics {self.id}>'

