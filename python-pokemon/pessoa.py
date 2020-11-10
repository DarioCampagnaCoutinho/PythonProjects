import random

from pokemon import *


NOMES = ['Dario', 'Malcon', 'Joaquin', 'Maria', 'Joana', 'Amadeu', 'John', 'Oliver', 'Felicity', 'Diggle', 'Barry']

POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarp"),
]


class Pessoa:
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemos(self):
        if self.pokemons:
            print('Pokemons de {}'.format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print('{} não tem nenhum pokemon.'.format(self))


class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capiturou {}'.format(self, pokemon))


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))
        super().__init__(nome=nome, pokemons=pokemons)

