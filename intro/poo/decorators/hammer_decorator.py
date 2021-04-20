from intro.poo.decorators.character_decorator import CharacterDecorator

class HammerDecorator(CharacterDecorator):

    def __init__(self, character):
        self.character = character
        self.character.live += 100
        self.character.attack += 500

    def is_attacked(self, attack_comming):
        return self.character.is_attacked(attack_comming)