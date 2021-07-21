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
    name, species_url = species_details['name'], species_details['url']
    print('species url:'+species_url)
    species_api = requests.get(species_url)
    species_json = json.loads(species_api.text)
    evolution_url = species_json['evolution_chain']['url']
    print('evolution url:'+evolution_url)
    evolution_id = (evolution_url.split('/'))[-2]

    evolution_page = requests.get(evolution_url)
    #print(evolution_url)
    evolution_json = json.loads(evolution_page.text)

    evolution_chain_type(evolution_json)
    evolution_tree(pokemon,species_json, evolution_json)
    print('----------')

    return evolution_chain_type


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
        if second_evolution == None:
            pass
        else:

            print('{} -> {}'.format(first_evolution, second_evolution))


    if third_evolution != None:
        return first_evolution+second_evolution+third_evolution

    if second_evolution != None:
        return first_evolution+second_evolution

    else:
        return first_evolution 


def evolution_tree(pokemon, species_json, evolution_json,):
    base_forms = check_base_forms(species_json)

    if base_forms == 3:
        #forma meowth
        print('■ -> ■ ')
        print('■ -> ■ ')
        print('■ -> ■ ')

    if base_forms == 2:
        #conferir se é slowbro ou evoluçao normal
        if check_branched_evolution(evolution_json):
            print('    ■')
            print('■ <')
            print('    ■')
            print('')
            print('    ■')
            print('■ <')
            print('    ■')
        

    if base_forms == 1 :
        evo_lenght = get_evo_line_lenght
        branched_evo, second_evo_branches, third_evo_branches = check_branched_evolution(evolution_json)
        if branched_evo:
            if (second_evo_branches == 8 and third_evo_branches == 0):
                #evee
                print('■   ■   ■')
                print('  ↖ ↑ ↗')
                print('■ ← ■ → ■')
                print('  ↙ ↓ ↘')
                print('■   ■   ■')
            if (second_evo_branches == 4 and third_evo_branches == 0):
                print('■ -> ■ ')
                print('  -> ■ ')
                print('  -> ■ ') 
                print('  -> ■ ')   

            if (second_evo_branches == 3 and third_evo_branches == 0):
                print('  -> ■ ')
                print('■ -> ■ ')
                print('  -> ■ ')         

        
def get_evolution(pokemon):
    pokemon_api = requests.get(url='https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon.dex))
    pokemon_json = json.loads(pokemon_api.text)

    species_details = (pokemon_json['species'])
    name, species_url = species_details['name'], species_details['url']
    print('species url:'+species_url)
    species_api = requests.get(species_url)
    species_json = json.loads(species_api.text)
    evolution_url = species_json['evolution_chain']['url']
    print('evolution url:'+evolution_url)
    evolution_id = (evolution_url.split('/'))[-2]

    evolution_page = requests.get(evolution_url)
    evolution_json = json.loads(evolution_page.text)

    first_evolution = evolution_json['chain']['species']['name']
    second_evolution = None;
    third_evolution = None;
    pokemon_list = []
    pokemon_list.append(call_pokemon(first_evolution))

    try:
        #arrumar para branched evolutions
        second_evolution = evolution_json['chain']['evolves_to'][0]['species']['name']
        pokemon_list.append(call_pokemon(second_evolution))

    except IndexError:
        pass
     
    try:
        #arrumar para branched evolutions
        third_evolution = evolution_json['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']
        pokemon_list.append(call_pokemon(third_evolution))

    except IndexError:
        pass
    list_iter = iter(pokemon_list)
    for pokemon_in_list in list_iter:
        if (pokemon_in_list == pokemon):
            try:
                return next(list_iter)
            except:
                return None




def check_base_forms(species_json):
    base_forms = 1
    for element in species_json['varieties']:
        if (element['is_default'] == True):
            pass

        if (element['is_default'] == False ):
            
            if ('alola' in element['pokemon']['name']) or ('galar' in  element['pokemon']['name']):
                base_forms = base_forms + 1

    return base_forms


def get_evo_line_lenght(evolution_json):
    evolution_line_lenght = 1
    try:
        second_evolution = evolution_json['chain']['evolves_to'][0]['species']['name']
        evolution_line_lenght = evolution_line_lenght + 1
            
    except:
        pass
     
    try:
        third_evolution = evolution_json['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']
        evolution_line_lenght = evolution_line_lenght + 1

    except:
        pass
    return evolution_line_lenght


def check_branched_evolution(evolution_json):
    evo_lenght = get_evo_line_lenght(evolution_json)
    second_evo_branches = 0
    third_evo_branches = 0
    try:
        second_evolution = evolution_json['chain']['evolves_to']
        evolution_list = []
        for evolution in second_evolution:
            evolution_list.append(evolution['species']['name'])
        if len(evolution_list)>1:
                print('branched evolution')
        branched_evolution = True
        second_evo_branches = len(evolution_list)
        try:
            second_evolution = evolution_json['chain']['evolves_to']
            another_evolution_list = []
            for evolution in second_evolution:
                for another_evolution in evolution['evolves_to']:
                    another_evolution_list.append(another_evolution['species']['name'])
            if another_evolution_list > 1:
                #branched third evo
                branched_evolution = True
                third_evo_branches = len(another_evolution_list)

        except:
            pass
        
    except:
        branched_evolution = False

    return branched_evolution, second_evo_branches, third_evo_branches




if __name__ == "__main__":

    get_evolution_json(call_pokemon(52))
    get_evolution_json(call_pokemon(79))
    get_evolution_json(call_pokemon(133))
    get_evolution_json(call_pokemon(106))
    get_evolution_json(call_pokemon(412))
    #next_evo = get_evolution(call_pokemon(2))
    #check_regional_form(call_pokemon(19))

