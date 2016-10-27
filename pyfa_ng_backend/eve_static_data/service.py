

from ..extensions import cache
from .models import InvCategory, InvMarketGroups, DgmTypeEffects
from .consts import dogma_effects_slots, market_groups_filter


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
        filtered_groups = self._filter_market_groups(market_groups)

        return filtered_groups

    @staticmethod
    def _filter_market_groups(market_groups):
        good_groups = []
        good_group_ids = []

        while True:
            new_good_groups = False

            for group in market_groups:
                if group.marketGroupID not in good_group_ids:
                    if group.parentGroupID is None and group.marketGroupID in market_groups_filter:
                        good_groups.append(group)
                        good_group_ids.append(group.marketGroupID)
                        new_good_groups = True

                    elif group.parentGroupID in good_group_ids:
                        good_groups.append(group)
                        good_group_ids.append(group.marketGroupID)
                        new_good_groups = True

            if new_good_groups is False:
                break

        return good_groups

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
