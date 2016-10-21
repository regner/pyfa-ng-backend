

from eos import Fit, Ship, Rig, Implant, Drone
from webargs import fields
from webargs.flaskparser import use_args
from flask_restful import Resource, reqparse

from .utils import build_high_module, build_mid_module, build_low_module


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
        fit = Fit()
        fit.ship = Ship(args['ship'])

        for high in args['high_slots']:
            module = build_high_module(high['id'], high['state'], high['charge'])
            fit.modules.high.equip(module)

        for mid in args['mid_slots']:
            module = build_mid_module(mid['id'], mid['state'], mid['charge'])
            fit.modules.med.equip(module)

        for low in args['low_slots']:
            module = build_low_module(low['id'], low['state'], low['charge'])
            fit.modules.low.equip(module)

        for rig in args['rigs']:
            fit.rigs.equip(Rig(rig))

        for implant in args['implants']:
            fit.implants.add(Implant(implant))

        for drone in args['drones']:
            fit.drones.add(Drone(drone['id'], drone['state']))

        # fit.validate()

        return {}, 200
