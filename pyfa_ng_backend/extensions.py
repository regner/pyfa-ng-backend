

from eos import SourceManager, JsonDataHandler, JsonCacheHandler

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache


db = SQLAlchemy()
migrate = Migrate()
cache = Cache()


def configure_extensions(app):
    """Registers all relevant extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)

    # Eos isn't a proper Flask extension at this time but it still needs app config to but initialized.
    # If we decide we want to support multiple sources or share this with other Flask applications
    # we should consider turning this into an extension.
    data_handler = JsonDataHandler(app.config['EOS_JSON_DATA'])
    cache_handler = JsonCacheHandler(app.config['EOS_CACHE'])
    SourceManager.add('tq', data_handler, cache_handler, make_default=True)
