# from sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# Import model classes
from.user import User
from.energy_record import EnergyRecord
from.analytics import Analytics