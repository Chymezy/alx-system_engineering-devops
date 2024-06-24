import unittest
from flask import Flask
from flask_testing import TestCase
from backend.app import app, db
from backend.models.user import User
from backend.models.energy_record import EnergyRecord
from backend.models.analytics import Analytics
from backend.routes import register_routes

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestingConfig')
        register_routes(app)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestAuthAPI(BaseTestCase):
    def test_auth(self):
        # Example test case for authentication
        response = self.client.post('/api/auth', json={
            'username': 'admin',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

class TestUserAPI(BaseTestCase):
    def test_create_user(self):
        response = self.client.post('/api/user', json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)
    
    def test_get_user(self):
        # First create a user
        user = User(username='testuser', email='testuser@example.com')
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()

        # Then get the user
        response = self.client.get('/api/user')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', str(response.data))

class TestEnergyAPI(BaseTestCase):
    def test_create_energy_record(self):
        # First create a user
        user = User(username='testuser', email='testuser@example.com')
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/api/energy', json={
            'user_id': user.id,
            'energy_consumed': 100.5
        })
        self.assertEqual(response.status_code, 201)

    def test_get_energy_records(self):
        # First create a user
        user = User(username='testuser', email='testuser@example.com')
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()

        # Create an energy record
        record = EnergyRecord(user_id=user.id, energy_consumed=100.5)
        db.session.add(record)
        db.session.commit()

        response = self.client.get('/api/energy', json={'user_id': user.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn('100.5', str(response.data))

class TestAnalyticsAPI(BaseTestCase):
    def test_create_analytics(self):
        # First create a user
        user = User(username='testuser', email='testuser@example.com')
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/api/analytics', json={
            'user_id': user.id,
            'metric': 'energy_efficiency',
            'value': 85.0
        })
        self.assertEqual(response.status_code, 201)

    def test_get_analytics(self):
        # First create a user
        user = User(username='testuser', email='testuser@example.com')
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()

        # Create an analytics record
        analytics = Analytics(user_id=user.id, metric='energy_efficiency', value=85.0)
        db.session.add(analytics)
        db.session.commit()

        response = self.client.get('/api/analytics', json={'user_id': user.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn('energy_efficiency', str(response.data))

if __name__ == '__main__':
    unittest.main()
