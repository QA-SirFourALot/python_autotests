import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 4888

def test_get_trainers_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_my_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == "4888"

def test_trainer_name(): 
    response_get_name = requests.get(url= f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get_name.json()["data"] [0] ["trainer_name"] == 'Фурало44'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Фурало44'), ('id', str(TRAINER_ID)),])

def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
