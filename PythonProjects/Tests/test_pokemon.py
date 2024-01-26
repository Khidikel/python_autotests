import pytest
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token': 'bad7f832d5f3c844b3aadd8e5857939a'}

def test_get_trainers():
    """
    Get trainer ID
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3564}, headers=HEADER, timeout=5)
    assert response.status_code ==200, 'Unexpected status code'