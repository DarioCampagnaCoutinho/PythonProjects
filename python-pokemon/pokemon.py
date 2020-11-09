import random


class Pokemon:
    def __init__(self, especie, level=1, nome=None):
        self.especie = especie
        self.level = level
        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} ({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        print("{} atacou {}".format(self, pokemon))


class PokemonEletrico(Pokemon):
    tipo = 'elétrico'

    def atacar(self, pokemon):
        print("{} lançou um raio de trovão {}".format(self, pokemon))


class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo {}".format(self, pokemon))


class PokemonAgua(Pokemon):
    tipo = 'água'

    def atacar(self, pokemon):
        print("{} lançou um jato de água {}".format(self, pokemon))