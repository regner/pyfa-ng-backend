

from ..extensions import cache
from .models import InvCategory, InvGroup, InvType, InvMarketGroups


class EVEStaticDataService(object):
    @cache.memoize()
    def get_tyes_by_category(self, category_id):
        category = InvCategory.query.filter_by(categoryID=category_id).first()

        types = []
        for group in category.groups:
            for t in group.types:
                types.append(t)

        return types

    @cache.memoize()
    def get_market_groups(self):
        market_groups = InvMarketGroups.query.all()
        return market_groups


eve_static_data_service = EVEStaticDataService()
