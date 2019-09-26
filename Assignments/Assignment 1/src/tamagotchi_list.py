from tamagotchi import Tamagotchi
from mussolini import Mussolini
from napoleon import Napoleon
from stalin import Stalin


class TamagotchiList:
    """
    List of all the tamagotchis used in the game.
    """
    _tam_list = [Mussolini(), Stalin(), Napoleon()]

    @classmethod
    def get_tam_list(cls):
        return cls._tam_list
