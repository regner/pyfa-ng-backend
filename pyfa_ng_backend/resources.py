

from .pyfa_eos import PyfaEosResource
from .fits import FitsResource


def configure_resources(api):
    """Configures all resources for the API."""
    api.add_resource(PyfaEosResource, '/eos/')
    api.add_resource(FitsResource, '/fits/')
