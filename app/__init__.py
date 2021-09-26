from flask import Flask
from .config import Config
from app.user import user
from app.habits import habits
from .extensions import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(user)
    app.register_blueprint(habits)

    return app
