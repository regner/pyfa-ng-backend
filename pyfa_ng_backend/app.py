

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from .config import AppConfig
from .extensions import configure_extensions
from .resources import configure_resources


def create_app():
    """Creates the Flask app object."""
    app = Flask(__name__)
    app.config.from_object(AppConfig)

    api = Api(app)
    CORS(app)

    configure_extensions(app)
    configure_resources(api)

    return app
