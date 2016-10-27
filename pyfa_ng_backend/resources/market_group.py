

from flask_restful import Resource

from ..eve_static_data import eve_static_data_service, consts


class MarketGroup(Resource):
    @staticmethod
    def convert_effect_to_slot(effect_id):
        if effect_id is consts.high_slot:
            return 'high'
        elif effect_id is consts.mid_slot:
            return 'mid'
        elif effect_id is consts.low_slot:
            return 'low'
        elif effect_id is consts.rig_slot:
            return 'rig'
        elif effect_id is consts.sub_system_slot:
            return 'sub_system'
        else:
            return None

    def convert_type_to_response(self, item):
        slot = eve_static_data_service.get_type_fitting_slot(item.typeID)

        return {
            'id': item.typeID,
            'name': item.typeName,
            'slot': self.convert_effect_to_slot(slot),
        }

    def get(self, market_group_id):
        market_group = eve_static_data_service.get_market_group(market_group_id)

        if market_group is not None:
            response = [self.convert_type_to_response(x) for x in market_group.types]

        else:
            response = []

        return response, 200
