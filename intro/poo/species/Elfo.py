from intro.poo.Specie import Specie


class Elfo(Specie):
    def __init__(self, name, size, height, age):
        super().__init__(name, size, height, age)
        self.live = 2000
        self.attack = 200

    def obtain_specie(self):
        return 'Elfo'