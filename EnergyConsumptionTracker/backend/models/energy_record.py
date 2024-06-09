from backend.utils.db import db
from datetime import datetime

class EnergyRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    energy_consumed = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('energy_records', lazy=True))

    def __repr__(self):
        return f'<EnergyRecord {self.id} for User {self.user_id}>'

