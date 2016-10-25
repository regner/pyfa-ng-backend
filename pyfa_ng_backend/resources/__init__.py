

from .market_groups import MarketGroups
from .fit_validation import FitValidation


def configure_resources(api):
    """Configures all resources for the API."""
    api.add_resource(MarketGroups, '/market_groups/')
    api.add_resource(FitValidation, '/fit_validation/')
