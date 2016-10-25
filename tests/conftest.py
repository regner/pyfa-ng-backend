

import pytest

from pyfa_ng_backend import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def full_fit():
    return {
        'ship': 32311,
        'high_slots': [
            {'id': 2929, 'state': 'online', 'charge': 12779},
            {'id': 2929, 'state': 'offline', 'charge': 12779},
            {'id': 2929, 'state': 'overload', 'charge': 12779},
        ],
        'mid_slots': [
            {'id': 5945, 'state': 'overload'},
            {'id': 4833, 'state': 'active', 'charge': 32014},
            {'id': 9622, 'state': 'offline'},
            {'id': 5443, 'state': 'overload'},
            {'id': 2281, 'state': 'overload'},
        ],
        'low_slots': [
            {'id': 2048, 'state': 'online'},
            {'id': 519, 'state': 'active'},
            {'id': 519, 'state': 'active'},
            {'id': 4405, 'state': 'active'},
            {'id': 4405, 'state': 'active'},
            {'id': 4405, 'state': 'offline'},
        ],
        'rigs': [
            26082,
            26088,
            26088,
        ],
        'drones': [
            {'id': 2446, 'state': 'active'},
            {'id': 2446, 'state': 'active'},
            {'id': 2446, 'state': 'active'},
            {'id': 2446, 'state': 'active'},
            {'id': 2446, 'state': 'active'},
            {'id': 2446, 'state': 'offline'},
            {'id': 2446, 'state': 'offline'},
            {'id': 2446, 'state': 'offline'},
        ],
        'implants': [
            13219,
            10228,
            24663,
            13244,
        ],
    }
