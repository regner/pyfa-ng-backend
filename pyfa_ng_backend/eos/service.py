

from eos import Fit, Ship, ModuleHigh, ModuleMed, ModuleLow, Rig, Implant, Drone, Charge


class EosService(object):
    def build_high_module(self, type_id, state, charge_type_id):
        return self._build_module(ModuleHigh, type_id, state, charge_type_id)

    def build_mid_module(self, type_id, state, charge_type_id):
        return self._build_module(ModuleMed, type_id, state, charge_type_id)

    def build_low_module(self, type_id, state, charge_type_id):
        return self._build_module(ModuleLow, type_id, state, charge_type_id)

    def _build_module(self, module_class, type_id, state, charge_type_id):
        if charge_type_id is not None:
            charge = Charge(charge_type_id)
        else:
            charge = None

        return module_class(type_id, state, charge)

    @staticmethod
    def build_rig(type_id):
        return Rig(type_id)

    @staticmethod
    def build_implant(type_id):
        return Implant(type_id)

    @staticmethod
    def build_drone(type_id, state):
        return Drone(type_id, state)

    @staticmethod
    def build_ship(type_id):
        return Ship(type_id)

    @staticmethod
    def build_full_fit(ship, highs=None, mids=None, lows=None, rigs=None, implants=None, drones=None):
        fit = Fit()
        fit.ship = ship

        if highs is not None:
            for hi in highs:
                fit.modules.high.equip(hi)

        if mids is not None:
            for mid in mids:
                fit.modules.medium.equip(mid)

        if lows is not None:
            for lo in lows:
                fit.modules.low.equip(lo)

        if rigs is not None:
            for rig in rigs:
                fit.rigs.equip(rig)

        if implants is not None:
            for imp in implants:
                fit.implants.equip(imp)

        if drones is not None:
            for drone in drones:
                fit.drones.equip(drone)

        return fit


eos_service = EosService()
