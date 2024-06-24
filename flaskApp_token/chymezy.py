from flask import request, Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import request, jsonify

# Initialize the app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/pld_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

# Define the User model
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

# Define the User API resource
class UserAPI(Resource):
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
            print("Error occurred:", str(e))
            return {'message': f'Internal server error: {str(e)}'}, 500

    def post(self):
        try:
            data = request.get_json()
            print("Received data:", data)

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
# Add resources to the API
api.add_resource(UserAPI, '/api/user')

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)
