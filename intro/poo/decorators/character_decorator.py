from intro.poo.Specie import Specie


class CharacterDecorator(Specie):
    def __init__(self, character):
        self.character = character

    def is_attacked(self, attack_comming):
        return self.character.is_attacked(attack_comming)