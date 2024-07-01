from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    full_name = db.Column(db.String(100))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=True)
    country = db.Column(db.String(100))
    sex = db.Column(db.String(10))
    user_type = db.Column(db.String(50))
    profile_picture = db.Column(db.LargeBinary)

    analytics = db.relationship('Analytics', back_populates='user', lazy=True)
    energy_records = db.relationship('EnergyRecord', back_populates='user', lazy=True)
    energy_savings = db.relationship('EnergySaving', back_populates='user', lazy=True)
    city = db.relationship('City', back_populates='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'city': self.city.name if self.city else None,
            'country': self.country,
            'sex': self.sex,
            'user_type': self.user_type,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
