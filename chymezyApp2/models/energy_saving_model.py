from extensions import db
from datetime import datetime

class EnergySaving(db.Model):
    __tablename__ = 'energy_saving'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    energy_record_id = db.Column(db.Integer, db.ForeignKey('energy_record.id'), nullable=False, index=True)
    saved_kwh = db.Column(db.Float, nullable=False)
    money_saved = db.Column(db.Float, nullable=False)
    calculation_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    user = db.relationship('User', back_populates='energy_saving', lazy=True)
    energy_record = db.relationship('EnergyRecord', back_populates='energy_saving', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "energy_record_id": self.energy_record_id,
            "saved_kwh": self.saved_kwh,
            "money_saved": self.money_saved,
            "calculation_date": self.calculation_date.isoformat()
        }
