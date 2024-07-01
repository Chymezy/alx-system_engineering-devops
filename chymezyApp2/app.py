from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import Config
from extensions import db, migrate, jwt
from routes.user_route import UserAPI, AuthAPI, TokenRefreshAPI
from routes.analytics_route import AnalyticsAPI
from routes.energy_record_route import EnergyRecordAPI
from routes.city_route import CityAPI
from routes.energy_benchmark_route import EnergyBenchmarkAPI
from routes.energy_saving_route import EnergySavingAPI
import json
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)

    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return super().default(obj)

    app.json_encoder = CustomJSONEncoder

    api = Api(app)
    api.add_resource(UserAPI, '/api/user')
    api.add_resource(AuthAPI, '/api/auth/login')
    api.add_resource(TokenRefreshAPI, '/api/auth/refresh')
    api.add_resource(AnalyticsAPI, '/api/analytics')
    api.add_resource(EnergyRecordAPI, '/api/energy_records', endpoint='energy_records')
    api.add_resource(EnergyRecordAPI, '/api/energy_records/<int:record_id>', endpoint='energy_record')
    api.add_resource(CityAPI, '/api/cities', endpoint='cities')
    api.add_resource(CityAPI, '/api/cities/<int:city_id>', endpoint='city')
    api.add_resource(EnergyBenchmarkAPI, '/api/energy_benchmarks', endpoint='energy_benchmarks')
    api.add_resource(EnergyBenchmarkAPI, '/api/energy_benchmarks/<int:benchmark_id>', endpoint='energy_benchmark')
    api.add_resource(EnergySavingAPI, '/api/energy_savings', endpoint='energy_savings')
    api.add_resource(EnergySavingAPI, '/api/energy_savings/<int:saving_id>', endpoint='energy_saving')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=4444, debug=True)
