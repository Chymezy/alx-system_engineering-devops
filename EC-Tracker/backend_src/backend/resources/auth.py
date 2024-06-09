from flask_restful import Resource, reqparse
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models import User

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username cannot be blank')
parser.add_argument('password', type=str, required=True, help='Password cannot be blank')
parser.add_argument('email', type=str, required=True, help='Email cannot be blank')

class Register(Resource):
    def post(self):
        data = parser.parse_args()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        
        new_user = User(username=data['username'], email=data['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"message": "User registered successfully"}), 201

class Login(Resource):
    def post(self):
        data = parser.parse_args()
        user = User.query.filter_by(username=data['username']).first()
        
        if user and check_password_hash(user.password, data['password']):
            return jsonify({"message": "Login successful", "user_id": user.id}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401

class Logout(Resource):
    def post(self):
        # Implement logout logic (e.g., token invalidation)
        return jsonify({"message": "Logout successful"}), 200

