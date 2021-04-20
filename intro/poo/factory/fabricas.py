from intro.poo.species.Breton import Breton
from intro.poo.species.Elfo import Elfo
from intro.poo.species.Imperial import Imperial
from intro.poo.species.Ogro import Ogro
from intro.poo.species.Argoniano import Argoniano


class FabricaPersonaje:

    def crear_personaje(self, specie, name, size, height, age):
        if specie == 'Argoniano':
            return Argoniano(name, size, height, age)
        elif specie == 'Breton':
            return Breton(name, size, height, age)
        elif specie == 'Elfo':
            return Elfo(name, size, height, age)
        elif specie == 'Imperial':
            return Imperial(name, size, height, age)
        elif specie == 'Ogro':
            return Ogro(name, size, height, age)

    def __init__(self, specie, name, size, height, age):
        self.personaje = self.crear_personaje(specie, name, size, height, age)