

from eos import ValidationError
from webargs import fields
from webargs.flaskparser import use_args
from flask_restful import Resource

from .service import pyfa_eos_service as pes


class PyfaEosResource(Resource):
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

    @staticmethod
    def convert_fit_to_response(fit):
        dps = fit.stats.get_nominal_dps(reload=False)
        dps_reload = fit.stats.get_nominal_dps(reload=True)

        return {
            'cpu': {
                'used': fit.stats.cpu.used,
                'output': fit.stats.cpu.output,
            },
            'powergrid': {
                'used': fit.stats.powergrid.used,
                'output': fit.stats.powergrid.output,
            },
            'calibration': {
                'used': fit.stats.calibration.used,
                'output': fit.stats.calibration.output,
            },
            'dronebay': {
                'used': fit.stats.dronebay.used,
                'output': fit.stats.dronebay.output,
            },
            'drone_bandwidth': {
                'used': fit.stats.drone_bandwidth.used,
                'output': fit.stats.drone_bandwidth.output,
            },
            'high_slots': {
                'used': fit.stats.high_slots.used,
                'total': fit.stats.high_slots.total,
            },
            'med_slots': {
                'used': fit.stats.med_slots.used,
                'total': fit.stats.med_slots.total,
            },
            'low_slots': {
                'used': fit.stats.low_slots.used,
                'total': fit.stats.low_slots.total,
            },
            'rig_slots': {
                'used': fit.stats.rig_slots.used,
                'total': fit.stats.rig_slots.total,
            },
            'subsystem_slots': {
                'used': fit.stats.subsystem_slots.used,
                'total': fit.stats.subsystem_slots.total,
            },
            'turret_slots': {
                'used': fit.stats.turret_slots.used,
                'total': fit.stats.turret_slots.total,
            },
            'launcher_slots': {
                'used': fit.stats.launcher_slots.used,
                'total': fit.stats.launcher_slots.total,
            },
            'launched_drones': {
                'used': fit.stats.launched_drones.used,
                'total': fit.stats.launched_drones.total,
            },
            'damage': {
                'reload': {
                    'em': dps_reload.em,
                    'thermal': dps_reload.thermal,
                    'kinetic': dps_reload.kinetic,
                    'explosive': dps_reload.explosive,
                    'total': dps_reload.total,
                },
                'no_reload': {
                    'em': dps.em,
                    'thermal': dps.thermal,
                    'kinetic': dps.kinetic,
                    'explosive': dps.explosive,
                    'total': dps.total,
                },
            },
        }

    @use_args(eos_fit_args)
    def post(self, args):
        ship = pes.build_ship(args['ship'])
        highs = [pes.build_high_module(x['id'], x['state'], x['charge']) for x in args['high_slots']]
        mids = [pes.build_mid_module(x['id'], x['state'], x['charge']) for x in args['mid_slots']]
        lows = [pes.build_low_module(x['id'], x['state'], x['charge']) for x in args['low_slots']]
        rigs = [pes.build_rig(x) for x in args['rigs']]
        implants = [pes.build_implant(x) for x in args['implants']]
        drones = [pes.build_drone(x['id'], x['state']) for x in args['drones']]

        skills = pes.build_all_v_character()

        fit = pes.build_full_fit(ship, skills, highs, mids, lows, rigs, implants, drones)
        fit.validate()

        return self.convert_fit_to_response(fit), 200
