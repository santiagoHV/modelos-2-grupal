from intro.poo.decorators.character_decorator import CharacterDecorator

class HelmetDecorator(CharacterDecorator):

    def __init__(self, character):
        self.character = character
        self.character.live += 200
        self.character.attack += 50

    def is_attacked(self, attack_comming):
        return self.character.is_attacked(attack_comming)