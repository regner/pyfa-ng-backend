

from flask_restful import Resource

from ..eve_static_data import eve_static_data_service


class MarketGroups(Resource):
    def get(self):
        market_groups = eve_static_data_service.get_market_groups()
        response = [
            {
                'id': x.marketGroupID,
                'parent': x.parentGroupID,
                'name': x.marketGroupName,
                'has_types': bool(x.hasTypes),
            } for x in market_groups
        ]

        return response, 200
