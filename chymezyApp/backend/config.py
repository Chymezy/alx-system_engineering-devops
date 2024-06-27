from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@127.0.0.1/pld_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    SECRET_KEY = os.getenv("SECRET_KEY")

    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ADMIN_USERNAME=os.getenv("ADMIN_USERNAME")
    ADMIN_PASSWORD=os.getenv("ADMIN_PASSWORD")

