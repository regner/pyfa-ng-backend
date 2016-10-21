

import json
import pytest

from manage import app


class TestEosResource:
    def setup_class(self):
        """Setup the test class."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        self.eos_route = '/eos/'

    def test_missing_ship_aborts(self):
        """Not including a ship ID should abort with correct error."""
        response = self.client.post(self.eos_route, data={})
        json_response = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 400
        assert json_response == {
            'message':
                {
                    'ship': 'Type ID for the ship being fit.',
                },
        }

    def test_full_fit(self):
        """Test a full fit gets parsed correctly."""
        data = {
            'ship': 1,
            'high_slots': [
                {'id': 333, 'state': 'online', 'charge': 12779},
                {'id': 333, 'state': 'offline', 'charge': 12779},
                {'id': 333, 'state': 'overload', 'charge': 24519},
            ],
            'mid_slots': [
                {'id': 222, 'state': 'online'},
                {'id': 222, 'state': 'active'},
                {'id': 222, 'state': 'offline', 'charge': 0},
                {'id': 222, 'state': 'overload', 'charge': 0},
            ],
            'low_slots': [
                {'id': 111, 'state': 'online'},
                {'id': 111, 'state': 'active'},
                {'id': 111, 'state': 'offline'},
            ],
            'rigs': [
                1234,
                12345,
                123456,
            ],
            'drones': [
                {'id': 9876, 'state': 'active'},
                {'id': 9876, 'state': 'active'},
                {'id': 9876, 'state': 'active'},
                {'id': 9876, 'state': 'offline'},
                {'id': 9876, 'state': 'offline'},
                {'id': 9876, 'state': 'offline'},
            ],
            'implants': [
                0000,
                1111,
                2222,
                3333,
            ],
            'boosters': [
                55,
                66,
                77,
            ]
        }

        response = self.client.post(self.eos_route, data=json.dumps(data))

        assert response.status_code == 200
