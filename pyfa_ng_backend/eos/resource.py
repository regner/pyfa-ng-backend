


from webargs import fields
from webargs.flaskparser import use_args
from flask_restful import Resource, reqparse

from .service import eos_service as es


class EosResource(Resource):
    module_args = fields.Nested({
        'id': fields.Int(required=True),
        'state': fields.Str(required=True),
        'charge': fields.Int(missing=None),
    })

    drone_args = fields.Nested({
        'id': fields.Int(required=True),
        'state': fields.Str(required=True),
    })

    eos_fit_args = {
        'ship': fields.Int(required=True),
        'rigs': fields.List(fields.Int(), missing=[]),
        'implants': fields.List(fields.Int(), missing=[]),
        'high_slots': fields.List(module_args, missing=[]),
        'mid_slots': fields.List(module_args, missing=[]),
        'low_slots': fields.List(module_args, missing=[]),
        'drones': fields.List(drone_args, missing=[]),
    }

    @use_args(eos_fit_args)
    def post(self, args):
        ship = es.build_ship(args['ship'])
        highs = [es.build_high_module(x['id'], x['state'], x['charge']) for x in args['high_slots']]
        mids = [es.build_mid_module(x['id'], x['state'], x['charge']) for x in args['mid_slots']]
        lows = [es.build_low_module(x['id'], x['state'], x['charge']) for x in args['low_slots']]
        rigs = [es.build_rig(x) for x in args['rigs']]
        implants = [es.build_implant(x) for x in args['implants']]
        drones = [es.build_drone(x['id'], x['state']) for x in args['drones']]

        fit = es.build_full_fit(ship, highs, mids, lows, rigs, implants, drones)

        return {}, 200
