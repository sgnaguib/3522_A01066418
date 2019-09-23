import tamagotchi
from mussolini import Mussolini
from napoleon import Napoleon
from stalin import Stalin

import random


class Game:
    """Represents a new user interaction with the tamagotchi game"""

    def __init__(self):
        self.tamagotchi = self.generate_rand_tamagotchi()


    def generate_rand_tamagotchi(self):
        """
        :return: a randomly selected tamagotchi
        """
        rand = random.randint(1, 3)
        tamagotchi_dict = {1: Mussolini(), 2: Napoleon(), 3: Stalin()}
        return tamagotchi_dict.get(rand)
