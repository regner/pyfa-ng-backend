

from .models import InvCategory, InvGroup, InvType


class EVEStaticDataService(object):
    def get_tyes_by_category(self, category_id):
        category = InvCategory.query.filter_by(categoryID=category_id).first()

        types = []
        for group in category.groups:
            for t in group.types:
                types.append(t)

        return types

eve_static_data_service = EVEStaticDataService()
