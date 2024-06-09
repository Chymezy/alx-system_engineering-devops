from flask import Flask
from backend.config import Config
from backend.routes import auth, user, energy, analytics
from backend.utils.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(energy.bp)
    app.register_blueprint(analytics.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

