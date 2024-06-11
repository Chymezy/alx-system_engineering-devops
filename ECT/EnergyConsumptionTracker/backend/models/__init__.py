from backend.utils.db import db
from backend.models.user import User
from backend.models.energy_record import EnergyRecord
from backend.models.analytics import Analytics


# psuedo: Importance: Sets up ORM system, enabling easy interaction with the database using Python objects.

# Initialize SQLAlchemy
db = SQLAlchemy()

# Import model classes

