

from .market_group import MarketGroup
from .market_groups import MarketGroups
from .fit_validation import FitValidation


def configure_resources(api):
    """Configures all resources for the API."""
    api.add_resource(MarketGroups, '/market_groups/')
    api.add_resource(MarketGroup, '/market_groups/<int:market_group_id>/')
    api.add_resource(FitValidation, '/fit_validation/')
