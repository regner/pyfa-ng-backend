

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

        self.full_fit = {
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

    def test_missing_ship_aborts(self):
        """Not including a ship ID should abort with correct error."""
        data = {}

        response = self.client.post(self.eos_route, data=json.dumps(data), content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 422
        assert json_response == {
            'messages':
                {
                    'ship': ['Missing data for required field.'],
                },
        }

    def test_no_high_slots_parses(self):
        """Test that if we don't pass high_slots it still parses."""
        data = self.full_fit.copy()
        del data['high_slots']

        response = self.client.post(self.eos_route, data=json.dumps(data), content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert json_response == {}

    def test_no_mid_slots_parses(self):
        """Test that if we don't pass mid_slots it still parses."""
        data = self.full_fit.copy()
        del data['mid_slots']

        response = self.client.post(self.eos_route, data=json.dumps(data), content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert json_response == {}

    def test_no_low_slots_parses(self):
        """Test that if we don't pass low_slots it still parses."""
        data = self.full_fit.copy()
        del data['low_slots']

        response = self.client.post(self.eos_route, data=json.dumps(data), content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert json_response == {}

    def test_no_rigs_parses(self):
        """Test that if we don't pass rigs it still parses."""
        data = self.full_fit.copy()
        del data['rigs']

        response = self.client.post(self.eos_route, data=json.dumps(data), content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert json_response == {}

    def test_no_drones_parses(self):
        """Test that if we don't pass drones it still parses."""
        data = self.full_fit.copy()
        del data['drones']

        response = self.client.post(self.eos_route, data=json.dumps(data), content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert json_response == {}

    def test_no_implants_parses(self):
        """Test that if we don't pass implants it still parses."""
        data = self.full_fit.copy()
        del data['implants']

        response = self.client.post(self.eos_route, data=json.dumps(data), content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert json_response == {}

    def test_full_fit(self):
        """Test a full fit gets parsed correctly."""
        response = self.client.post(self.eos_route, data=json.dumps(self.full_fit), content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert json_response == {}
