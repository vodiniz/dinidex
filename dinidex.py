import pypokedex

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
    print('Sprinte{}'.format(pokemon.sprites))
    
    return


def main():
    print('Digite o nome de um pokemon')
    input_pokemon = input()
    pokemon = call_pokemon(input_pokemon)
    print(pokemon)
    print_pokemon(pokemon)

main()

