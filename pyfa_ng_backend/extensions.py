

from eos import SourceManager, JsonDataHandler, JsonCacheHandler

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()

data_handler = JsonDataHandler('eve_data/phobos_dump/')
cache_handler = JsonCacheHandler('eve_data/pyfa_cache/eos_tq.json.bz2')
SourceManager.add('tq', data_handler, cache_handler, make_default=True)


def configure_extensions(app):
    """Registers all relevant extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
