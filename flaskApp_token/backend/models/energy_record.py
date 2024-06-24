# from datetime import datetime
# from backend.utils.db import db

# class EnergyRecord(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     energy_consumed = db.Column(db.Float, nullable=False)
#     timestamp = db.Column(db.DateTime, default=datetime.now)
    
#     user = db.relationship('User', backref=db.backref('energy_records', lazy=True))

#     def __repr__(self):
#         return f'<EnergyRecord {self.id} - User {self.user_id}>'

from backend.utils.db import db

class EnergyRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    energy_consumption = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "energy_consumption": self.energy_consumption,
            "timestamp": self.timestamp
        }
    
    def __repr__(self):
        return f'<EnergyRecord {self.id} - User {self.user_id}>'


