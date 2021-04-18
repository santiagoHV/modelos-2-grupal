from intro.poo.Specie import Specie
from intro.poo.decorators.character_decorator import CharacterDecorator


class armour_decorator(CharacterDecorator):
    def __init__(self, character):
        self.character = character
        self.character.live = self.character.live * 1.1
        self.character.attack = self.character.attack * 2

    def is_attacked(self, attack_comming):
        return self.character.is_attacked(attack_comming)