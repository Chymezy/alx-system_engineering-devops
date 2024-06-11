from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from backend.models.user import User
from backend.utils.db import db


#Importance: Manages user authentication.

class AuthAPI(Resource):
    # Define POST method for login
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            token = create_access_token(identity=user.id)
            return {'token': token}, 200
        return {'message': 'Invalid credentials'}, 401

