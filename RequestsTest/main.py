import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8824e3db76c292afab30b4cee960a38f'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
          
body_confirmation = {"trainer_token": TOKEN}
body_create = {
    "name": "Бульбазав",
    "photo_id": 8
}
body_changename = {
    "pokemon_id": "67471",
    "name": "Бульбазаурус",
    "photo_id": 8
}

pokemon_id = {
    "pokemon_id": "67471"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.text)

response_changename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changename)
print(response_changename.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = pokemon_id)
print(response_add_pokeball.text)