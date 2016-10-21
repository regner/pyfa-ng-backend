

import os


class AppConfig(object):
    """Config object for the app that pulls from the environment."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('PYFA_SQLA_URI', 'postgresql://postgres:db@host')
