from flask import Flask
from app.config import load_configurations, configure_logging
from .routes import data_blueprint
from .services.transaction import transaction_blueprint


def create_app():
    app = Flask(__name__)

    # Load configurations and logging settings
    load_configurations(app)
    configure_logging()

    # Import and register blueprints, if any
    app.register_blueprint(data_blueprint)
    app.register_blueprint(transaction_blueprint)

    return app
