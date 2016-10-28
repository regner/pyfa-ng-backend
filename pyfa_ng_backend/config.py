

import os


class AppConfig(object):
    """Config object for the app that pulls from the environment."""
    DEBUG = True
    CACHE_DEFAULT_TIMEOUT = os.environ.get('CACHE_DEFAULT_TIMEOUT', 600)
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')
    SQLALCHEMY_BINDS = {
        'sde': os.environ.get('SQLALCHEMY_SDE', 'sqlite:///../eve_data/static_data/tq.db'),
    }
    EOS_JSON_DATA = os.environ.get('EOS_JSON_DATA', 'eve_data/phobos_dump/')
    EOS_CACHE = os.environ.get('EOS_CACHE', 'eve_data/pyfa_cache/eos_tq.json.bz2')
