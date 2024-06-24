import unittest
from datetime import datetime
from backend.utils.db import db
from backend.app import app  # Import your Flask app object
from backend.models.user import User
from backend.models.energy_record import EnergyRecord

class TestEnergyRecord(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup Flask app context and database session
        cls.app = app  # Assign the Flask app object directly
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Clean up after all tests are done
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        # Create a user for testing
        self.user = User(username='testuser', email='test@example.com')
        self.user.set_password('testpassword')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        # Clean up after each test method
        db.session.delete(self.user)
        db.session.commit()

    def test_create_energy_record(self):
        # Create an energy record for the user
        energy_record = EnergyRecord(user_id=self.user.id, energy_consumed=100.0)
        db.session.add(energy_record)
        db.session.commit()

        # Retrieve the energy record from the database
        saved_record = EnergyRecord.query.filter_by(id=energy_record.id).first()

        # Assert that the saved record matches the created record
        self.assertIsNotNone(saved_record)
        self.assertEqual(saved_record.user_id, self.user.id)
        self.assertEqual(saved_record.energy_consumed, 100.0)
        self.assertIsInstance(saved_record.timestamp, datetime)

    def test_energy_record_representation(self):
        # Create an energy record
        energy_record = EnergyRecord(user_id=self.user.id, energy_consumed=100.0)
        db.session.add(energy_record)
        db.session.commit()

        # Assert the string representation matches expectations
        expected_repr = f'<EnergyRecord {energy_record.id} - User {self.user.id}>'
        self.assertEqual(repr(energy_record), expected_repr)

    def test_energy_record_relationship(self):
        # Create an energy record
        energy_record = EnergyRecord(user_id=self.user.id, energy_consumed=100.0)
        db.session.add(energy_record)
        db.session.commit()

        # Access the user associated with the energy record
        associated_user = energy_record.user

        # Assert that the associated user matches the original user
        self.assertEqual(associated_user.id, self.user.id)
        self.assertEqual(associated_user.username, 'testuser')

if __name__ == '__main__':
    unittest.main()

