
class Specie:

    def __init__(self, name, size, height, age):
        self._name = name
        self._size = size
        self._height = height
        self._age = age
        self._live = 0
        self._attack = 0


    def is_attacked(self, attack_comming):
        self._live -= attack_comming
        return self.live

    def obtain_specie(self):
        return 'no implementado'


    @property
    def name(self):
        return self._name


    @property
    def size(self):
        return self._size


    @property
    def height(self):
        return self._height


    @property
    def age(self):
        return self._age

    @property
    def live(self):
        return self._live

    @property
    def attack(self):
        return self._attack


    @name.setter
    def name(self, name):
        self._name = name


    @size.setter
    def size(self, size):
        self._size = size


    @height.setter
    def height(self, height):
        self._height = height


    @age.setter
    def age(self, age):
        self._age = age


    @live.setter
    def live(self, live):
        self._live = live


    @attack.setter
    def attack(self, attack):
        self._attack = attack








