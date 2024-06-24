# from flask import request
# from flask_restful import Resource
# from flask_jwt_extended import create_access_token
# from backend.models.user import User
# from backend.utils.db import db


# #Importance: Manages user authentication.

# class AuthAPI(Resource):
#     # Define POST method for login
#     def post(self):
#         data = request.get_json()
#         user = User.query.filter_by(username=data['username']).first()
#         if user and user.check_password(data['password']):
#             token = create_access_token(identity=user.id)
#             return {'token': token}, 200
#         return {'message': 'Invalid credentials'}, 401

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/api/auth', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # Authenticate the user here (e.g., check username and password against the database)
    if username != "test" or password != "test":  # This is just an example check
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
