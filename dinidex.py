import pypokedex
import json
import requests


def get_evolution_json(id):

    pokemon_api = requests.get(url='https://pokeapi.co/api/v2/pokemon/{}'.format(id))
    pokemon_json = json.loads(pokemon_api.text)

    species_api = (pokemon_json['species'])
    name, evolution_url = species_api['name'], species_api['url']
    print(evolution_url)
    evolution_api = requests.get(evolution_url)
    evolution_json = json.loads(evolution_api.text)
    evolution_url = evolution_json['evolution_chain']['url']
    evolution_id = (evolution_url.split('/'))[-2]

    evolution_page = requests.get(evolution_url)
    evolution_chain = json.loads(evolution_page.text)

    return evolution_chain



def call_pokemon(input):
    try:
        input = int(input)
        pokemon = pypokedex.get(dex=input)

    except ValueError:
        pokemon = pypokedex.get(name=input)

    return pokemon

def print_pokemon(pokemon):
    print('Dex:#{}'.format(pokemon.dex))
    print('Name:{}'.format(pokemon.name))
    print('Height:{}'.format(pokemon.height))
    print('Weight:{}'.format(pokemon.weight))
    print('Types:{}'.format(pokemon.types))
    print('Abilities:{}'.format(pokemon.abilities))
    print('Stats:{}'.format(pokemon.base_stats))
    print(list(pokemon.get_descriptions().values())[0])
    print(pokemon.moves)

    return














def main():
    print('Digite o nome de um pokemon')
    input_pokemon = input()
    pokemon = call_pokemon(input_pokemon)
    print(pokemon)
    print_pokemon(pokemon)

main()

