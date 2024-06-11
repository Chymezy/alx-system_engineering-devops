import os

#psuedo codes: Importance: Centralizes configuration management for different environments.

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "my_jwt_secret")

