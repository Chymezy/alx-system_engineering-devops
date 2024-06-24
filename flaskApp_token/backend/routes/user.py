# from flask import request
# from flask_restful import Resource
# from backend.models.user import User
# from backend.utils.db import db

# #Importance: Manages user-related operations.


# class UserAPI(Resource):
#     # Define POST method for creating a user
#     def post(self):
#         data = request.get_json()
#         if User.query.filter_by(username=data['username']).first():
#             return {'message': 'User already exists'}, 400
#         user = User(username=data['username'])
#         user.set_password(data['password'])
#         db.session.add(user)
#         db.session.commit()
#         return {'message': 'User created'}, 201

#     # Define GET method for retrieving a user
#     def get(self, user_id):
#         user = User.query.get_or_404(user_id)
#         return user.to_dict(), 200

from flask import request
from flask_restful import Resource
from backend.models.user import User
from backend.utils.db import db

class UserAPI(Resource):
    def post(self):
        try:
            data = request.get_json() # what if is not in a json format?
            print("Received data:", data)  # Debugging line to print received data

            # Validate required fields
            if not data:
                print("No input data provided")
                return {'message': 'No input data provided'}, 400
            if 'username' not in data or not data['username']:
                print("Username is required")
                return {'message': 'Username is required'}, 400
            if 'password' not in data or not data['password']:
                print("Password is required")
                return {'message': 'Password is required'}, 400
            if 'email' not in data or not data['email']:
                print("Email is required")
                return {'message': 'Email is required'}, 400

        #     # Check if the user already exists
        #     existing_user = User.query.filter_by(username=data['username']).first()
        #     if existing_user:
        #         print("User already exists")
        #         return {'message': 'User already exists'}, 400

        #     # Create the user
        #     user = User(username=data['username'], email=data['email'])
        #     user.set_password(data['password'])
        #     db.session.add(user)
        #     db.session.commit()
        #     print("User created successfully")
        #     return {'message': 'User created'}, 201

        except Exception as e:
            print("Error occurred:", str(e))
            return {'message': 'Internal server error'}, 500
