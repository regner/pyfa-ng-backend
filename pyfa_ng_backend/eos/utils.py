

from eos import ModuleHigh, ModuleMed, ModuleLow, Charge


def build_high_module(type_id, state, charge_type_id):
    return build_module(ModuleHigh, type_id, state, charge_type_id)


def build_mid_module(type_id, state, charge_type_id):
    return build_module(ModuleMed, type_id, state, charge_type_id)


def build_low_module(type_id, state, charge_type_id):
    return build_module(ModuleLow, type_id, state, charge_type_id)


def build_module(module_class, type_id, state, charge_type_id):
    if charge_type_id is not None:
        charge = Charge(charge_type_id)
    else:
        charge = None

    return module_class(type_id, state, charge)