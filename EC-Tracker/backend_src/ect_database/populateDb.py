from app import app, db
from models import User, EnergyRecord
from werkzeug.security import generate_password_hash
from datetime import date

def populate_db():
    with app.app_context():
        # Create some users
        user1 = User(username='user1', email='user1@example.com', password=generate_password_hash('password1'))
        user2 = User(username='user2', email='user2@example.com', password=generate_password_hash('password2'))

        # Add users to the session
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        # Create some energy records
        record1 = EnergyRecord(user_id=user1.id, date=date(2024, 6, 1), consumption=10.5)
        record2 = EnergyRecord(user_id=user1.id, date=date(2024, 6, 2), consumption=11.0)
        record3 = EnergyRecord(user_id=user2.id, date=date(2024, 6, 1), consumption=9.0)
        record4 = EnergyRecord(user_id=user2.id, date=date(2024, 6, 2), consumption=8.5)

        # Add records to the session
        db.session.add(record1)
        db.session.add(record2)
        db.session.add(record3)
        db.session.add(record4)
        db.session.commit()

if __name__ == '__main__':
    populate_db()
    print("Database populated successfully!")

