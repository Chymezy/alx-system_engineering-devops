# # from flask import Blueprint
# # from flask_restful import Api
# # from backend.routes.auth import AuthAPI
# # from backend.routes.energy import EnergyAPI
# # from backend.routes.user import UserAPI
# # from backend.routes.analytics import AnalyticsAPI


# # # Importance: Aggregates and registers all API routes.

# # def register_routes(app):
# #     # Initialize Blueprint and Api
# #     blueprint = Blueprint('api', __name__)
# #     api = Api(blueprint)

# #     # Register RESTful resource routes for authentication, energy, user, and analytics endpoints
# #     api.add_resource(AuthAPI, '/auth')
# #     api.add_resource(EnergyAPI, '/energy')
# #     api.add_resource(UserAPI, '/user')
# #     api.add_resource(AnalyticsAPI, '/analytics')

# #     app.register_blueprint(blueprint, url_prefix='/api')

# # __all__ = ["analytics", "auth", "energy", "user"]

# # backend/routes/__init__.py

# from flask import Blueprint
# from backend.routes.user import UserAPI
# from backend.routes.auth import AuthAPI
# from backend.routes.energy import EnergyAPI
# from backend.app import app  # Import the Flask app instance

# def register_routes(api):
#     # Create API blueprint
#     api_bp = Blueprint('api', __name__, url_prefix='/api')
    
#     # Register resource routes under the blueprint
#     api.add_resource(UserAPI, '/user', '/user/<int:user_id>')
#     api.add_resource(AuthAPI, '/auth')
#     api.add_resource(EnergyAPI, '/energy')
    
#     # Register blueprint with the app
#     app.register_blueprint(api_bp)


from flask import Blueprint
from flask_restful import Api
from backend.routes.user import UserAPI

def register_routes(app):
    api_bp = Blueprint('api', __name__, url_prefix='/api')
    api = Api(api_bp)

    api.add_resource(UserAPI, '/user')

    app.register_blueprint(api_bp)
