from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from backend.config import Config
from backend.utils.db import db
from backend.routes import register_routes

#psuedo codes
# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Set up CORS
CORS(app)

# Initialize database
db.init_app(app)

# Initialize JWT
jwt = JWTManager(app)

# Register routes
register_routes(app)

# Define root route to serve frontend
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)

