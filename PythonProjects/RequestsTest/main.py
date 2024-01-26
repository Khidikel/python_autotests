"""
test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token': 'bad7f832d5f3c844b3aadd8e5857939a'}

response = requests.post(url=f'{URL}/pokemons', json={
    "name": "Буль",
   "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}.Сообщение:{response.text})')

json_data=response.json()

response = requests.put(url=f'{URL}/pokemons', json={
    "pokemon_id": "28636",
    "name": "QWERTY",
   "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}.Сообщение:{response.text})')

json_data=response.json()

response = requests.post(url=f'{URL}/trainers/add_pokeball', json={
    "pokemon_id": "28551"
}, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}.Сообщение:{response.text})')

json_data=response.json()
  
