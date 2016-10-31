

import json

from collections import namedtuple


MARKET_GROUPS_URL = '/market_groups/'

MarketGroup = namedtuple(
    'MarketGroup',
    ['marketGroupID', 'parentGroupID', 'marketGroupName', 'description', 'iconID', 'hasTypes'],
    verbose=True
)


def test_market_groups(mocker, client):
    """Test that the market groups resource requests and formats the correct information."""
    static_data_service = mocker.patch('pyfa_ng_backend.resources.market_groups.eve_static_data_service')
    static_data_service.get_market_groups.return_value = [
        MarketGroup(1, None, 'Test One', 'description', 0, 0),
        MarketGroup(2, None, 'Test Two', 'description', 0, 1),
        MarketGroup(3, 2, 'Test Three', 'description', 0, 0),
        MarketGroup(4, 3, 'Test Four', 'description', 0, 1),
    ]

    response = client.get(MARKET_GROUPS_URL)
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == [
        {
            'id': 1,
            'parent': None,
            'name': 'Test One',
            'has_types': False,
        },
        {
            'id': 2,
            'parent': None,
            'name': 'Test Two',
            'has_types': True,
        },
        {
            'id': 3,
            'parent': 2,
            'name': 'Test Three',
            'has_types': False,
        },
        {
            'id': 4,
            'parent': 3,
            'name': 'Test Four',
            'has_types': True,
        },
    ]


def test_market_groups_has_cache_header(mocker, client):
    """Ensure that the market groups response has the Cache-Control header."""
    static_data_service = mocker.patch('pyfa_ng_backend.resources.market_group.eve_static_data_service')
    static_data_service.get_market_groups.return_value = []

    response = client.get(MARKET_GROUPS_URL)

    assert response.status_code == 200
    assert 'Cache-Control' in response.headers


