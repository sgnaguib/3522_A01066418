import tamagotchi
from mussolini import Mussolini
from napoleon import Napoleon
from stalin import Stalin
from cabbage import Cabbage
from baguette import Baguette
from spaghetti import Spaghetti

import random


class Game:
    """Represents a new user interaction with the tamagotchi game"""

    def __init__(self):
        self.tamagotchi = self.generate_rand_tamagotchi()
        self.food_list = [Cabbage(), Baguette(), Spaghetti()]


    def generate_rand_tamagotchi(self):
        """
        :return: a randomly selected tamagotchi
        """
        rand = random.randint(1, 3)
        tamagotchi_dict = {1: Mussolini(), 2: Napoleon(), 3: Stalin()}
        return tamagotchi_dict.get(rand)

    def feed_tamagotchi(self, food):
        """
        Determines the hunger value of the input food and
        decreases the tamagotchi's hunger by that value
        :return: string telling user how much the tamagotchi's
        hunger decreased.
        """
        for element in self.food_list:
            if element.name == food:
                hunger_value = element.hunger_value
                self.tamagotchi.decrease_hunger(hunger_value)

        return f"Yum. My hunger reduced by {hunger_value} points."
