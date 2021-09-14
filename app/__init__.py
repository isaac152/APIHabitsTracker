from flask import Flask
from .config import Config
from app.user import user
from app.habits import habits
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    jwt= JWTManager(app)
    app.register_blueprint(user)
    app.register_blueprint(habits)

    return app
