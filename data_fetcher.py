""" animals_data_fetcher.py
This script has functions to fetch animal data via API api-ninjas
"""


import requests

API_KEY = 'kq1HhmnSDWMP2pcRDLIIXA==5kUrqif7KOBwnxlB'




def fetch_data(animal_name):
    """ Fetches the animals data for the animal 'animal_name'.
    :return: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
          ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
    },
    """
    animals_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    res = requests.get(animals_url, headers={'X-Api-Key': API_KEY}, timeout=None)
    if res.status_code == 200:
        animals_data = res.json()

    else:
        print('Error:', res.status_code, res.text)
        animals_data = ''
    return animals_data