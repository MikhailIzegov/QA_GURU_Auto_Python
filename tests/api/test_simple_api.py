import jsonschema
import requests

from tests.api.utils.read_json import load_schema


def test_get_users_status_code():
    response = requests.get(url='https://reqres.in/api/users')

    assert response.status_code == 200


def test_get_users_per_page():
    response = requests.get(url='https://reqres.in/api/users', params={'per_page': 1})

    assert len(response.json()['data']) == 1
    assert response.json()['per_page'] == 1


def test_headers():
    response = requests.get(url='https://reqres.in/api/users', headers={'Connection': 'keep-alive'})

    assert 'Connection' in response.headers
    assert response.headers['Connection'] == 'keep-alive'


def test_create_user():
    response = requests.post(url='https://reqres.in/api/users', json={
            "name": "morpheus",
            "job": "leader"
    }
                             )
    # assert response.json()['name'] == 'morpheus'
    # assert response.json()['job'] == 'leader'

    # Валидация схемы
    schema = load_schema('post_users.json')
    assert response.status_code == 201
    jsonschema.validate(response.json(), schema)
