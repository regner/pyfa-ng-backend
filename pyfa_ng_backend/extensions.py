

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def configure_extensions(app):
    """Registers all relevant extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
