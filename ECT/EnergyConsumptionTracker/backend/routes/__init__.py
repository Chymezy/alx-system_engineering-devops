from flask import Blueprint
from flask_restful import Api
from backend.routes.auth import AuthAPI
from backend.routes.energy import EnergyAPI
from backend.routes.user import UserAPI
from backend.routes.analytics import AnalyticsAPI


# Importance: Aggregates and registers all API routes.

def register_routes(app):
    # Initialize Blueprint and Api
    blueprint = Blueprint('api', __name__)
    api = Api(blueprint)

    # Register RESTful resource routes for authentication, energy, user, and analytics endpoints
    api.add_resource(AuthAPI, '/auth')
    api.add_resource(EnergyAPI, '/energy')
    api.add_resource(UserAPI, '/user')
    api.add_resource(AnalyticsAPI, '/analytics')

    app.register_blueprint(blueprint, url_prefix='/api')

