from Intro.poo.Specie import Specie


class Imperial(Specie):
    def __init__(self, name, size, height, age):
        super().__init__(name, size, height, age)
        self.live = 2500
        self.attack = 350

    def obtain_specie(self):
        return 'Imperial'
