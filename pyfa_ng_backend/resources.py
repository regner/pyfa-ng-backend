

from .eos import EosResource
from .fits import FitsResource


def configure_resources(api):
    """Configures all resources for the API."""
    api.add_resource(EosResource, '/eos/')
    api.add_resource(FitsResource, '/fits/')
