import unittest
from datetime import datetime
from backend.utils.db import db
from backend.app import app  # Import your Flask app object
from backend.models.user import User
from backend.models.analytics import Analytics

class TestAnalytics(unittest.TestCase):

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

    def test_create_analytics_record(self):
        # Create an analytics record for the user
        analytics_data = {'metric': 100, 'type': 'daily'}
        analytics_record = Analytics(user_id=self.user.id, data=analytics_data)
        db.session.add(analytics_record)
        db.session.commit()

        # Retrieve the analytics record from the database
        saved_record = Analytics.query.filter_by(id=analytics_record.id).first()

        # Assert that the saved record matches the created record
        self.assertIsNotNone(saved_record)
        self.assertEqual(saved_record.user_id, self.user.id)
        self.assertEqual(saved_record.data, analytics_data)
        self.assertIsInstance(saved_record.created_at, datetime)

    def test_analytics_record_relationship(self):
        # Create an analytics record
        analytics_data = {'metric': 100, 'type': 'daily'}
        analytics_record = Analytics(user_id=self.user.id, data=analytics_data)
        db.session.add(analytics_record)
        db.session.commit()

        # Access the user associated with the analytics record
        associated_user = analytics_record.user

        # Assert that the associated user matches the original user
        self.assertEqual(associated_user.id, self.user.id)
        self.assertEqual(associated_user.username, 'testuser')

if __name__ == '__main__':
    unittest.main()

