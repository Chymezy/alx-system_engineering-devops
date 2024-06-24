# from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy.exc import IntegrityError
# from backend.utils.db import db

# import os
# import sys

# sys.path.insert(0, os.path.abspath('~/project/play_ground/flaskApp/backend/'))

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.now)
#     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

#     # Add the relationship with Analytics
#     analytics = db.relationship('Analytics', back_populates='user')

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     def __repr__(self):
#         return f'<User {self.username}>'

#     @classmethod
#     def create_user(cls, username, email, password):
#         try:
#             user = cls(username=username, email=email)
#             user.set_password(password)
#             db.session.add(user)
#             db.session.commit()
#             return user
#         except IntegrityError:
#             db.session.rollback()
#             return None

#     @classmethod
#     def get_user_by_id(cls, user_id):
#         return cls.query.get(user_id)

#     @classmethod
#     def get_user_by_username(cls, username):
#         return cls.query.filter_by(username=username).first()

#     @classmethod
#     def get_user_by_email(cls, email):
#         return cls.query.filter_by(email=email).first()

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'username': self.username,
#             'email': self.email,
#             'created_at': self.created_at,
#             'updated_at': self.updated_at
#         }

from datetime import datetime
from backend.utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
