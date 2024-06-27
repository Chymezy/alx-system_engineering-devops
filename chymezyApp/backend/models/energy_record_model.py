from extensions import db

class EnergyRecord(db.Model):
    __tablename__ = 'energy_record'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    consumption = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    user = db.relationship('User', back_populates='energy_records', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "consumption": self.consumption,
            "timestamp": self.timestamp.isoformat() 
        }

    def __repr__(self):
        return f'<EnergyRecord {self.id} - User {self.user_id}>'
