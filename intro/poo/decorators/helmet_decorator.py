from intro.poo.decorators.character_decorator import CharacterDecorator

class HelmetDecorator(CharacterDecorator):

    def __init__(self, character):
        self.character = character
        self.character.live = self.character.live * 3
        self.character.attack = self.character.attack * 1.2

    def is_attacked(self, attack_comming):
        return self.character.is_attacked(attack_comming)