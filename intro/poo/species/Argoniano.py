from intro.poo.Specie import Specie


class Argoniano(Specie):
    def __init__(self, name, size, height, age):
        super().__init__(name, size, height, age)
        self.live = 3000
        self.attack = 120

    def obtain_specie(self):
        return 'Argoniano'
