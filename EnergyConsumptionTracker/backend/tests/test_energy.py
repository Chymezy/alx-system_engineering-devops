import unittest
from backend.app import create_app
from backend.utils.db import db
from backend.models.energy_record import EnergyRecord
from backend.models.user import User

class EnergyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        self.user_id = user.id

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_energy_record(self):
        response = self.client.post('/api/energy', json={
            'user_id': self.user_id,
            'energy_consumed': 100.5
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('recordId', response.json)

if __name__ == '__main__':
    unittest.main()

