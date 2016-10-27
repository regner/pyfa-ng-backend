

from eos import Fit, Ship, ModuleHigh, ModuleMed, ModuleLow, Rig, Implant, Drone, Charge, State, Skill

from ..eve_static_data.consts import CAT_SKILLS
from ..extensions import cache
from ..eve_static_data import eve_static_data_service


class PyfaEosService(object):
    def build_high_module(self, type_id, state, charge_type_id):
        return self._build_module(ModuleHigh, type_id, state, charge_type_id)

    def build_mid_module(self, type_id, state, charge_type_id):
        return self._build_module(ModuleMed, type_id, state, charge_type_id)

    def build_low_module(self, type_id, state, charge_type_id):
        return self._build_module(ModuleLow, type_id, state, charge_type_id)

    def _build_module(self, module_class, type_id, state, charge_type_id):
        converted_state = self.convert_state(state)

        if charge_type_id is not None:
            charge = Charge(charge_type_id)
        else:
            charge = None

        if converted_state is not None:
            module = module_class(type_id, state=converted_state, charge=charge)

        else:
            module = module_class(type_id, charge=charge)

        return module

    @staticmethod
    def build_rig(type_id):
        return Rig(type_id)

    @staticmethod
    def build_implant(type_id):
        return Implant(type_id)

    def build_drone(self, type_id, state):
        converted_state = self.convert_state(state)

        if converted_state is not None:
            drone = Drone(type_id, state=converted_state)

        else:
            drone = Drone(type_id)

        return drone

    @staticmethod
    def build_ship(type_id):
        return Ship(type_id)

    @staticmethod
    def convert_state(state):
        if state is not None:
            if state is 'online':
                return State.online
            elif state is 'offline':
                return State.offline
            elif state is 'active':
                return State.active
            elif state is 'overload':
                return State.overload
        return None

    @staticmethod
    def build_full_fit(ship, skills=None, highs=None, mids=None, lows=None, rigs=None, implants=None, drones=None):
        fit = Fit()
        fit.ship = ship

        if skills is not None:
            for skill in skills:
                fit.skills.add(skill)

        if highs is not None:
            for hi in highs:
                fit.modules.high.equip(hi)

        if mids is not None:
            for mid in mids:
                fit.modules.med.equip(mid)

        if lows is not None:
            for lo in lows:
                fit.modules.low.equip(lo)

        if rigs is not None:
            for rig in rigs:
                fit.rigs.equip(rig)

        if implants is not None:
            for imp in implants:
                fit.implants.add(imp)

        if drones is not None:
            for drone in drones:
                fit.drones.add(drone)

        return fit

    @staticmethod
    def build_skill(skill_id, level=5):
        return Skill(skill_id, level)

    @cache.memoize()
    def build_all_v_character(self):
        skills_category = CAT_SKILLS
        skill_types = eve_static_data_service.get_types_by_category(skills_category)

        return [self.build_skill(x.typeID) for x in skill_types]


pyfa_eos_service = PyfaEosService()
