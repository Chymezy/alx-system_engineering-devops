from flask import request
from flask_restful import Resource
from backend.models.user import User
from backend.utils.db import db

#Importance: Manages user-related operations.


class UserAPI(Resource):
    # Define POST method for creating a user
    def post(self):
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return {'message': 'User already exists'}, 400
        user = User(username=data['username'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created'}, 201

    # Define GET method for retrieving a user
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user.to_dict(), 200

