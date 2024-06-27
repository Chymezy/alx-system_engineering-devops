from flask import Flask
from flask_restful import Api
from flask_cors import CORS  # Import CORS from flask_cors
from config import Config
from extensions import db, migrate, jwt
from routes.user_route import UserAPI, AuthAPI, TokenRefreshAPI
from routes.analytics_route import AnalyticsAPI
from routes.energy_record_route import EnergyRecordAPI
import json
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Enable CORS for all domains on all routes
    CORS(app)

    # Custom JSON encoder for handling datetime objects
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return super().default(obj)

    app.json_encoder = CustomJSONEncoder

    # Add resources to the API
    api = Api(app)
    api.add_resource(UserAPI, '/api/user')
    api.add_resource(AuthAPI, '/api/auth/login')
    api.add_resource(TokenRefreshAPI, '/api/auth/refresh')
    api.add_resource(AnalyticsAPI, '/api/analytics')
    api.add_resource(EnergyRecordAPI, '/api/energy_records', endpoint='energy_records')
    api.add_resource(EnergyRecordAPI, '/api/energy_records/<int:record_id>', endpoint='energy_record')



    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=4444, debug=True)
