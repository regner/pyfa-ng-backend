

import json


FIT_VALIDATION_URL = '/fit_validation/'


def test_missing_ship_aborts(client):
    """Not including a ship ID should abort with correct error."""
    data = {}

    response = client.post(FIT_VALIDATION_URL, data=json.dumps(data), content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 422
    assert json_response == {
        'messages':
            {
                'ship': ['Missing data for required field.'],
            },
    }


def test_no_high_slots_parses(mocker, client, full_fit):
    """Test that if we don't pass high_slots it still parses."""
    mocker.patch('pyfa_ng_backend.resources.fit_validation.pes')
    fit_response = mocker.patch('pyfa_ng_backend.resources.fit_validation.FitValidation.convert_fit_to_response')
    fit_response.return_value = {}

    data = full_fit.copy()
    del data['high_slots']

    response = client.post(FIT_VALIDATION_URL, data=json.dumps(data), content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == {}


def test_no_mid_slots_parses(mocker, client, full_fit):
    """Test that if we don't pass mid_slots it still parses."""
    mocker.patch('pyfa_ng_backend.resources.fit_validation.pes')
    fit_response = mocker.patch('pyfa_ng_backend.resources.fit_validation.FitValidation.convert_fit_to_response')
    fit_response.return_value = {}

    data = full_fit.copy()
    del data['mid_slots']

    response = client.post(FIT_VALIDATION_URL, data=json.dumps(data), content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == {}


def test_no_low_slots_parses(mocker, client, full_fit):
    """Test that if we don't pass low_slots it still parses."""
    mocker.patch('pyfa_ng_backend.resources.fit_validation.pes')
    fit_response = mocker.patch('pyfa_ng_backend.resources.fit_validation.FitValidation.convert_fit_to_response')
    fit_response.return_value = {}

    data = full_fit.copy()
    del data['low_slots']

    response = client.post(FIT_VALIDATION_URL, data=json.dumps(data), content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == {}


def test_no_rigs_parses(mocker, client, full_fit):
    """Test that if we don't pass rigs it still parses."""
    mocker.patch('pyfa_ng_backend.resources.fit_validation.pes')
    fit_response = mocker.patch('pyfa_ng_backend.resources.fit_validation.FitValidation.convert_fit_to_response')
    fit_response.return_value = {}

    data = full_fit.copy()
    del data['rigs']

    response = client.post(FIT_VALIDATION_URL, data=json.dumps(data), content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == {}


def test_no_drones_parses(mocker, client, full_fit):
    """Test that if we don't pass drones it still parses."""
    mocker.patch('pyfa_ng_backend.resources.fit_validation.pes')
    fit_response = mocker.patch('pyfa_ng_backend.resources.fit_validation.FitValidation.convert_fit_to_response')
    fit_response.return_value = {}

    data = full_fit.copy()
    del data['drones']

    response = client.post(FIT_VALIDATION_URL, data=json.dumps(data), content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == {}


def test_no_implants_parses(mocker, client, full_fit):
    """Test that if we don't pass implants it still parses."""
    mocker.patch('pyfa_ng_backend.resources.fit_validation.pes')
    fit_response = mocker.patch('pyfa_ng_backend.resources.fit_validation.FitValidation.convert_fit_to_response')
    fit_response.return_value = {}

    data = full_fit.copy()
    del data['implants']

    response = client.post(FIT_VALIDATION_URL, data=json.dumps(data), content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == {}


def test_full_fit(mocker, client, full_fit):
    """Test a full fit gets parsed correctly."""
    mocker.patch('pyfa_ng_backend.resources.fit_validation.pes')
    fit_response = mocker.patch('pyfa_ng_backend.resources.fit_validation.FitValidation.convert_fit_to_response')
    fit_response.return_value = {}

    response = client.post(FIT_VALIDATION_URL, data=json.dumps(full_fit), content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert json_response == {}


def test_lets_raise_an_error(client, full_fit):
    """Test causing an error gets caught correctly."""
    fit = full_fit.copy()
    fit['high_slots'].append({'id': 2929, 'state': 'online', 'charge': 12779})
    fit['high_slots'].append({'id': 2929, 'state': 'online', 'charge': 12779})
    fit['high_slots'].append({'id': 2929, 'state': 'online', 'charge': 12779})
    fit['high_slots'].append({'id': 2929, 'state': 'online', 'charge': 12779})
    fit['high_slots'].append({'id': 2929, 'state': 'online', 'charge': 12779})
    fit['high_slots'].append({'id': 2929, 'state': 'online', 'charge': 12779})
    fit['high_slots'].append({'id': 2929, 'state': 'online', 'charge': 12779})

    response = client.post(FIT_VALIDATION_URL, data=json.dumps(full_fit), content_type='application/json')
    json_response = json.loads(response.data.decode('utf-8'))
