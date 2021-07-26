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


def get_species_json(pokemon):
    pokemon_api = requests.get(url='https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon.dex))
    pokemon_json = json.loads(pokemon_api.text)
    species_details = (pokemon_json['species'])
    name, species_url = species_details['name'], species_details['url']
    species_api = requests.get(species_url)
    species_json = json.loads(species_api.text)

    return species_json, species_url

def get_evolution_json(species_json):
    evolution_url = species_json['evolution_chain']['url']
    evolution_id = (evolution_url.split('/'))[-2]
    evolution_page = requests.get(evolution_url)
    evolution_json = json.loads(evolution_page.text)

    return evolution_json, evolution_url

def get_simple_evolution_list(evolution_json):

    first_evolution_pokemon =call_pokemon(evolution_json['chain']['species']['name'])

    second_evolution_pokemon = get_evolution(first_evolution_pokemon, evolution_json)
    third_evolution_pokemon = get_evolution(second_evolution_pokemon, evolution_json)

    print(third_evolution_pokemon)
    
    if second_evolution_pokemon == None:
        print('{} '.format(first_evolution_pokemon.name))
        return first_evolution_pokemon

    else:
        pass

    if third_evolution_pokemon == None:
        print(first_evolution_pokemon.name, '->', end = '')
        for evolution in second_evolution_pokemon:
            if second_evolution_pokemon.index(evolution) != 0:
                print('/', end = '')
            print(evolution.name)
        
        second_evolution_pokemon.insert(0, first_evolution_pokemon)
        return second_evolution_pokemon

    else:
        print(first_evolution_pokemon.name, '->', end = '')
        for evolution in second_evolution_pokemon:
            if second_evolution_pokemon.index(evolution) != 0:
                print('/', end = '')
            print(evolution.name, end ='')
        print(first_evolution_pokemon.name, '->', end = '')
        for evolution in third_evolution_pokemon:
            print(evolution.name, end ='')
        second_evolution_pokemon.insert(0, first_evolution_pokemon)
        return second_evolution_pokemon + third_evolution_pokemon


   
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
    
def check_base_forms(species_json):

    for element in species_json['varieties']:
        if (element['is_default'] == True):
            pass

        if (element['is_default'] == False ):
            
            if ('alola' in element['pokemon']['name']) or ('galar' in  element['pokemon']['name']):
                base_forms = base_forms + 1

    return base_forms


def check_1_evo_base_forms(species_json):
    base_forms = 1
    if species_json['evolves_from_species'] == None:
        pass
    else:
        json_page = requests.get(species_json['evolves_from_species']['url'])
        species_json = json.loads(json_page.text)    
        for element in species_json['varieties']:
            if (element['is_default'] == True):
                pass

    if (element['is_default'] == False ):
        
        if ('alola' in element['pokemon']['name']) or ('galar' in  element['pokemon']['name']):
            base_forms = base_forms + 1

    return base_forms


def get_alternate_forms(species_json):
    alternate_form_list = []
    for element in species_json['varieties']:
        if (element['is_default'] == True):
            pass

        if (element['is_default'] == False ):
            
            if ('alola' in element['pokemon']['name']) or ('galar' in  element['pokemon']['name']):
                alternate_form_list.append(call_pokemon(element['pokemon']['name']))
    
    if len(alternate_form_list) > 0:
        return alternate_form_list
    else:
        return None

def check_branched_evolution(species_json, evolution_json):
    evo_lenght = get_evo_line_lenght(evolution_json)
    second_evo_branches = 0
    third_evo_branches = 0
    branched_evolution = False
    alternate_form_list = None
    pokemon_2_evolution = None
    try:
        second_evolution = evolution_json['chain']['evolves_to']
        evolution_list = []
        for evolution in second_evolution:
            pokemon_name = evolution['species']['name']
            evolution_list.append(pokemon_name)
            pokemon_2_evolution = call_pokemon(pokemon_name)
            pokemon_2_evolution_species_json = get_species_json(pokemon_2_evolution)
            alternate_form_list = get_alternate_forms(pokemon_2_evolution_species_json)
        
        if alternate_form_list == None:
            pass
        else:
            if len(alternate_form_list) >= len(check_1_evo_base_forms):
                for alternate_form in alternate_form_list:
                    evolution_list.append(alternate_form)

        if len(evolution_list)>1:
            print('branched evolution')
            branched_evolution = True
            second_evo_branches = len(evolution_list)
        
        try:
            another_evolution_list = []
            for evolution in second_evolution:
                for another_evolution in evolution['evolves_to']:
                    another_evolution_list.append(another_evolution['species']['name'])
                    pokemon_3_evolution = call_pokemon(pokemon_name)
                    pokemon_3_evolution_species_json = get_species_json(pokemon_3_evolution)
                    alternate_form_list = get_alternate_forms(pokemon_3_evolution_species_json)

                if alternate_form_list == None:
                    pass
                else:
                    if len(alternate_form_list) >= len(check_1_evo_base_forms):
                        for alternate_form in alternate_form_list:
                            another_evolution_list.append(alternate_form)

                    if len(another_evolution_list) > 1:
                        #branched third evo
                        branched_evolution = True
                        third_evo_branches = len(another_evolution_list)

        except:
            pass
        
    except:
        pass
    return branched_evolution, second_evo_branches, third_evo_branches


def print_evo_tree(pokemon, species_json, evolution_json):
    base_forms = check_base_forms(species_json)
    evo_lenght = get_evo_line_lenght(evolution_json)

    if evo_lenght ==1:
        print('■')

    if evo_lenght == 2:
        if base_forms == 3:
            #forma meowth
            print('■ -> ■ ')
            print('■ -> ■ ')
            print('■ -> ■ ')

        if base_forms == 2:
            #conferir se é slowbro ou evoluçao normal
            if check_branched_evolution(species_json, evolution_json):
                print('    ■')
                print('■ <')
                print('    ■')
                print('')
                print('    ■')
                print('■ <')
                print('    ■')
            
        if base_forms == 1 :
            branched_evo, second_evo_branches, third_evo_branches = check_branched_evolution(species_json,evolution_json)
            if branched_evo:
                if (second_evo_branches == 8):
                    #evee
                    print('■   ■   ■')
                    print('  ↖ ↑ ↗')
                    print('■ ← ■ → ■')
                    print('  ↙ ↓ ↘')
                    print('■   ■   ■')

                if (second_evo_branches == 3):
                    #TYROGUE
                    print('  -> ■ ')
                    print('■ -> ■ ')
                    print('  -> ■ ')

                if second_evo_branches == 2:
                    #CUBONE
                    print('    ■')
                    print('■ <')
                    print('    ■')          

    if evo_lenght == 3:
        if check_branched_evolution:
            print('branched evolution')

        else:
            print('■ -> ■ -> ■') 
    


def get_evolution(pokemon, evolution_json):
    #PROBLEMAS COM 3 EVOLUÇAO FAZER O CHECK
    return_list = []
    third_evo_check = False
    try: 
        if pokemon.name == evolution_json['chain']['species']['name']:
            for pokemon1 in evolution_json['chain']['evolves_to']:
                return_list.append(call_pokemon(pokemon1['species']['name']))
    except:
        return None
    
    try:
        for pokemon1 in evolution_json['chain']['evolves_to']:
            if pokemon.name == pokemon1['species']['name']:
                for pokemon2 in pokemon1['evolves_to']:
                    return_list.append(call_pokemon(pokemon2['species']['name']))
    except:
        pass

    try:
        for pokemon1 in evolution_json['chain']['evolves_to']:
            for pokemon2 in pokemon1['evolves_to']:
                print(pokemon2)
                if pokemon.name == pokemon1['species']['name']:
                    return None              
                else:
                    return_list.append(call_pokemon(pokemon2['species']['name']))    
    except:
        pass

    if len(return_list) == 0:
        return None
    else:
        return return_list


def test_return_evolution(pokemon):
    species_json, species_url = get_species_json(pokemon)
    evolution_json, evolution_url = get_evolution_json(species_json)
    return_pokemon = get_evolution(pokemon, evolution_json)
    get_simple_evolution_list(evolution_json)
    return return_pokemon


def get_evo_layout(pokemon):
    species_json, species_url = get_species_json(pokemon)
    evolution_json, evolution_url = get_species_json
    print('species url:'+species_url)
    print('evolution url:'+evolution_url)

    return





if __name__ == "__main__":

    # # get_evolution_json(call_pokemon(52))
    # # get_evolution_json(call_pokemon(79))
    # # get_evolution_json(call_pokemon(133))
    # get_evolution_json(call_pokemon(122))
    # get_evolution_json(call_pokemon(862))
    # get_evolution_json(call_pokemon(104))
    # #next_evo = get_evolution(call_pokemon(2))
    # #check_regional_form(call_pokemon(19))

    test_return_evolution(call_pokemon(input()))

