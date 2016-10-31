

import json

from collections import namedtuple

from pyfa_ng_backend.eve_static_data import consts


MARKET_GROUPS_URL = '/market_groups/61/'

InvType = namedtuple('InventoryType', ['typeID', 'typeName'], verbose=True)


class MarketGroup(object):
    @property
    def types(self):
        return [
            InvType(1, 'Test One'),
            InvType(2, 'Test Two'),
            InvType(3, 'Test Three'),
            InvType(4, 'Test Four'),
            InvType(5, 'Test Five'),
        ]


def test_market_group(mocker, client):
    """Test that the market groups resource requests and formats the correct information."""
    static_data_service = mocker.patch('pyfa_ng_backend.resources.market_group.eve_static_data_service')
    static_data_service.get_market_group.return_value = MarketGroup()
    static_data_service.get_type_fitting_slot.side_effect = consts.dogma_effects_slots

    response = client.get(MARKET_GROUPS_URL)
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == [
        {'id': 1, 'name': 'Test One', 'slot': 'high'},
        {'id': 2, 'name': 'Test Two', 'slot': 'mid'},
        {'id': 3, 'name': 'Test Three', 'slot': 'low'},
        {'id': 4, 'name': 'Test Four', 'slot': 'rig'},
        {'id': 5, 'name': 'Test Five', 'slot': 'sub_system'},
    ]


def test_market_group_handles_none(mocker, client):
    """Ensure that if there are no types in a market group we handle it gracefully."""
    static_data_service = mocker.patch('pyfa_ng_backend.resources.market_group.eve_static_data_service')
    static_data_service.get_market_group.return_value = None

    response = client.get(MARKET_GROUPS_URL)
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == []


def test_market_groups_has_cache_header(mocker, client):
    """Ensure that the market groups response has the Cache-Control header."""
    static_data_service = mocker.patch('pyfa_ng_backend.resources.market_group.eve_static_data_service')
    static_data_service.get_market_groups.return_value = []

    response = client.get(MARKET_GROUPS_URL)

    assert response.status_code == 200
    assert 'Cache-Control' in response.headers
