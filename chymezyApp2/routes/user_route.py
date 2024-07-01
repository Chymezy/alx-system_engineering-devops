from models.user_model import User
from extensions import db
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity


class UserAPI(Resource):
    @jwt_required()
    def get(self):
        try:
            username = request.args.get('username')
            if not username:
                return {'message': 'Username is required'}, 400

            user = User.query.filter_by(username=username).first()
            if not user:
                return {'message': 'User not found'}, 404

            return jsonify(user.to_dict())

        except Exception as e:
            return {'message': f'Internal server error: {str(e)}'}, 500

    def post(self):
        try:
            data = request.get_json()
            # Validate required fields
            if not data:
                return {'message': 'No input data provided'}, 400
            if 'username' not in data or not data['username']:
                return {'message': 'Username is required'}, 400
            if 'password' not in data or not data['password']:
                return {'message': 'Password is required'}, 400
            if 'email' not in data or not data['email']:
                return {'message': 'Email is required'}, 400

            # Check if the user already exists
            existing_user = User.query.filter_by(username=data['username']).first()
            if existing_user:
                print("User already exists")
                return {'message': 'User already exists'}, 400

            # Create the user
            user = User(username=data['username'], email=data['email'])
            user.set_password(data['password'])
            db.session.add(user)
            db.session.commit()
            print("User created successfully")
            return {'message': 'User created'}, 201

        except Exception as e:
            print("Error occurred:", str(e))
            return {'message': f'Internal server error: {str(e)}'}, 500

class AuthAPI(Resource):
    def post(self):
        try:
            data = request.get_json()
            if not data or 'username' not in data or 'password' not in data:
                return {'message': 'Username and password are required'}, 400

            user = User.query.filter_by(username=data['username']).first()
            if not user or not user.check_password(data['password']):
                return {'message': 'Invalid credentials'}, 401

            access_token = create_access_token(identity=user.username)
            refresh_token = create_refresh_token(identity=user.username)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        except Exception as e:
            print("Error occurred:", str(e))
            return {'message': f'Internal server error: {str(e)}'}, 500

class TokenRefreshAPI(Resource):
    @jwt_required(refresh=True)
    def post(self):
        try:
            current_user = get_jwt_identity()
            access_token = create_access_token(identity=current_user)
            return {'access_token': access_token}, 200

        except Exception as e:
            print("Error occurred:", str(e))
            return {'message': f'Internal server error: {str(e)}'}, 500
