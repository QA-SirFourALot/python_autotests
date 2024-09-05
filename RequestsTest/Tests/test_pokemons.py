import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8824e3db76c292afab30b4cee960a38f'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 4888

def test_get_trainers_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_my_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == "4888"
