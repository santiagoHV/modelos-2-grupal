from Intro.poo.Specie import Specie


class Ogro(Specie):
    def __init__(self, name, size, height, age):
        super().__init__(name, size, height, age)
        self.live = 5000
        self.attack = 500

    def obtain_specie(self):
        return 'Ogro'