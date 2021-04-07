from Intro.poo.Specie import Specie


class Breton(Specie):
    def __init__(self, name, size, height, age):
        super().__init__(name, size, height, age)
        self.live = 1800
        self.attack = 300

    def obtain_specie(self):
        return 'Breton'
