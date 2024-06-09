from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    api = Api(app)

    from resources.user import UserRegister, UserLogin, UserLogout
    from resources.energy import EnergyRecordResource, EnergyRecordListResource
    from resources.analytics import AnalyticsResource

    api.add_resource(UserRegister, '/api/users')
    api.add_resource(UserLogin, '/api/auth/login')
    api.add_resource(UserLogout, '/api/auth/logout')
    api.add_resource(EnergyRecordResource, '/api/energy/<int:id>')
    api.add_resource(EnergyRecordListResource, '/api/energy')
    api.add_resource(AnalyticsResource, '/api/analytics')

    return app

