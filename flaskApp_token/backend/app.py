# from flask import Flask, jsonify, send_from_directory
# from flask_migrate import Migrate
# from flask_cors import CORS
# from flask_jwt_extended import JWTManager
# from backend.config import Config
# from backend.utils.db import db
# from backend.routes import register_routes

# import os
# # import sys
# # sys.path.append(os.path.dirname(os.path.abspath(__file__))) # debugg add
# # sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # debugg add

# #psuedo codes
# # Initialize Flask app
# app = Flask(__name__)
# app.config.from_object(Config)

# # Set up CORS
# CORS(app)

# # Initialize database
# db.init_app(app)
# migrate = Migrate(app, db) # newly added by me

# # Initialize JWT
# jwt = JWTManager(app)

# # Register routes
# register_routes(app)

# #Define root route to serve frontend
# @app.route("/", defaults={"path": ""})
# @app.route("/<path:path>")
# def serve(path):
#     if path != "" and os.path.exists(app.static_folder + "/" + path):
#         return send_from_directory(app.static_folder, path)
#     else:
#         return send_from_directory(app.static_folder, "index.html")

# @app.route("/test_db")
# def test_db():
#     try:
#         # Attempt to execute a simple query
#         result = db.engine.execute('SELECT 1')
#         return jsonify({"success": True, "message": "Database connection successful"})
#     except Exception as e:
#         return jsonify({"success": False, "message": str(e)})

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')

# backend/app.py

# backend/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from werkzeug.security import generate_password_hash, check_password_hash
from backend.routes.user import UserAPI

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/pld_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Add resources to the API
api.add_resource(UserAPI, '/api/user')

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
