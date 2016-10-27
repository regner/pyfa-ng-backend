

from ..extensions import cache
from .models import InvCategory, InvMarketGroups, DgmTypeEffects
from .consts import dogma_effects_slots


class EVEStaticDataService(object):
    @cache.memoize()
    def get_types_by_category(self, category_id):
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

    @cache.memoize()
    def get_market_group(self, group_id):
        return InvMarketGroups.query.filter_by(marketGroupID=group_id).first()

    @cache.memoize()
    def get_type_fitting_slot(self, type_id):
        effect = DgmTypeEffects\
            .query\
            .filter_by(typeID=type_id)\
            .filter(DgmTypeEffects.effectID.in_(dogma_effects_slots))\
            .first()

        if effect is not None:
            return effect.effectID
        return None


eve_static_data_service = EVEStaticDataService()
