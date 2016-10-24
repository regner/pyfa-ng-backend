

import os


class AppConfig(object):
    """Config object for the app that pulls from the environment."""
    DEBUG = True
    CACHE_TYPE = 'simple'
    SQLALCHEMY_BINDS = {
        'sde': 'sqlite:///../eve_data/static_data/tq.db',
    }
