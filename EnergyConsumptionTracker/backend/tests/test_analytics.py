import unittest
from backend.app import create_app
from backend.utils.db import db
from backend.models.analytics import Analytics

class AnalyticsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        analytics = Analytics(total_energy_consumed=500.0)
        db.session.add(analytics)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_analytics(self):
        response = self.client.get('/api/analytics')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 0)

if __name__ == '__main__':
    unittest.main()

