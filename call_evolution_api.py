import json
import requests


def get_pokemon_api(id):

    pokemon_api = requests.get(url='https://pokeapi.co/api/v2/pokemon/{}'.format(id))
    pokemon_json = json.loads(pokemon_api.text)

    species_api = (pokemon_json['species'])
    name, evolution_url = species_api['name'], species_api['url']
    print(evolution_url)
    evolution_api = requests.get(evolution_url)
    evolution_json = json.loads(evolution_api.text)
    evolution_url = evolution_json['evolution_chain']['url']
    evolution_id = (evolution_url.split('/'))[-2]

    get_evolution_details(evolution_url)



    return evolution_url


def get_evolution_details(url):
    evolution_page = requests.get(url)
    evolution_chain = json.loads(evolution_page.text)
    return


id = "gloom"

pokemon = get_pokemon_api(id)

