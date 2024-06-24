# backend/tests/test_user_model.py
import unittest
from datetime import datetime
from backend.models.user import User
from backend.utils.db import db

class TestUserModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up any necessary resources before running the tests
        pass

    @classmethod
    def tearDownClass(cls):
        # Clean up after running all the tests, if necessary
        pass

    def setUp(self):
        # Set up any resources specific to each test case
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        self.user = User(username=self.user_data['username'], email=self.user_data['email'])
        self.user.set_password(self.user_data['password'])

    def tearDown(self):
        # Clean up after each test case
        db.session.rollback()

    def test_create_user(self):
        # Test creating a new user
        db.session.add(self.user)
        db.session.commit()
        self.assertIsNotNone(self.user.id)
        self.assertEqual(self.user.username, self.user_data['username'])
        self.assertTrue(self.user.check_password(self.user_data['password']))

    def test_get_user_by_id(self):
        # Test retrieving user by ID
        db.session.add(self.user)
        db.session.commit()
        retrieved_user = User.get_user_by_id(self.user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.id, self.user.id)

    def test_get_user_by_username(self):
        # Test retrieving user by username
        db.session.add(self.user)
        db.session.commit()
        retrieved_user = User.get_user_by_username(self.user.username)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, self.user.username)

    def test_get_user_by_email(self):
        # Test retrieving user by email
        db.session.add(self.user)
        db.session.commit()
        retrieved_user = User.get_user_by_email(self.user.email)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, self.user.email)

    def test_set_password(self):
        # Test setting and checking password
        self.user.set_password('newpassword456')
        self.assertTrue(self.user.check_password('newpassword456'))
        self.assertFalse(self.user.check_password(self.user_data['password']))  # Ensure old password doesn't work

    def test_create_duplicate_user(self):
        # Test creating a user with duplicate username
        db.session.add(self.user)
        db.session.commit()
        duplicate_user = User(username=self.user_data['username'], email='anotheruser@example.com')
        db.session.add(duplicate_user)
        with self.assertRaises(Exception):
            db.session.commit()

if __name__ == '__main__':
    unittest.main()

