from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import Config
from .models import db
from .user import user_bp
from .energy import energy_bp
from .analytics import analytics_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(user_bp)
app.register_blueprint(energy_bp)
app.register_blueprint(analytics_bp)

if __name__ == "__main__":
    app.run(debug=True)

