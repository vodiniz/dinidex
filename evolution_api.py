import json
import requests
import pypokedex

def call_pokemon(input):
    try:
            input = int(input)
            pokemon = pypokedex.get(dex=input)
    except:
            pokemon = pypokedex.get(name=input)

    return pokemon

def get_evolution_json(pokemon):

    pokemon_api = requests.get(url='https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon.dex))
    pokemon_json = json.loads(pokemon_api.text)

    species_details = (pokemon_json['species'])
    name, evolution_url = species_details['name'], species_details['url']
    print('{} evolution line'.format(name))
    species_api = requests.get(evolution_url)
    species_json = json.loads(species_api.text)
    evolution_url = species_json['evolution_chain']['url']
    evolution_id = (evolution_url.split('/'))[-2]

    evolution_page = requests.get(evolution_url)
    #print(evolution_url)
    evolution_json = json.loads(evolution_page.text)

    evolution_chain_type(evolution_json)

    return evolution_chain_type

def check_regional_form(pokemon, evolution_json):
    dex = pokemon.dex
    species_url = 'https://pokeapi.co/api/v2/pokemon-species/{}/'.format(dex)
    species_page = requests.get(species_url)
    species_json = json.loads(species_page.text)
    base_forms = 1
    evolution1_forms = None

    
    for element in species_json['varieties']:
        if (['is_default'] == True):
            pass

        if (['is_default'] == False ):
            if ('alola' in element['pokemon']['name']) or ('galar' in  element['pokemon']['name']):
                base_forms = base_forms + 1

    return


def evolution_chain_type(json):

    first_evolution = json['chain']['species']['name']
    second_evolution = None;
    third_evolution = None;

    try:
        second_evolution = json['chain']['evolves_to'][0]['species']['name']

    except IndexError:
        print('{} '.format(first_evolution))
     
    try:
        third_evolution = json['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']
        print('{} -> {} -> {}'.format(first_evolution, second_evolution,third_evolution))

    except IndexError:
        print('{} -> {}'.format(first_evolution, second_evolution))

    if third_evolution != None:
        return first_evolution+second_evolution+third_evolution

    if second_evolution != None:
        return first_evolution+second_evolution

    else:
        return first_evolution 



if __name__ == "__main__":

    #get_evolution_json(call_pokemon(115))
    #get_evolution_json(1)
    #get_evolution_json(25)
    check_regional_form(call_pokemon(19))

