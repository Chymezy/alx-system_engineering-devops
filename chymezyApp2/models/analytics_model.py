from datetime import datetime
from extensions import db

class Analytics(db.Model):
    __tablename__ = 'analytics'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    data = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user = db.relationship('User', back_populates='analytics', lazy=True)

    # Updated __init__ method to accept user_id instead of username
    def __init__(self, user_id, data):
        self.user_id = user_id
        self.data = data

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'data': self.data,
            'created_at': self.created_at.isoformat()
        }