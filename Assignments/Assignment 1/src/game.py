import tamagotchi
from mussolini import Mussolini
from napoleon import Napoleon
from stalin import Stalin
from timekeeper import TimeKeeper
from foodlist import FoodList
from activitylist import ActivityList

import random


class Game:
    """Represents a new user interaction with the tamagotchi game"""

    def __init__(self):
        self.tamagotchi = self.generate_rand_tamagotchi()
        self.food_list = FoodList().get_food_list()
        self.act_list = ActivityList().get_act_list()
        TimeKeeper.time_check()

    def update_status(self):
        self.tamagotchi.update_status(TimeKeeper.time_check())

    def check_status(self):
        # print(TimeKeeper.time_check())
        self.update_status()
        return self.tamagotchi.check_status()

    def get_message(self):
        return self.tamagotchi.message()


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
                chosen_food = element

        hunger_value = chosen_food.hunger_value
        self.tamagotchi.decrease_hunger(chosen_food.hunger_value)

        if chosen_food.name in self.tamagotchi.preferred_food:
            self.tamagotchi.decrease_hunger(
                chosen_food.hunger_value*0.1)
            hunger_value *= 1.1

        return f"Yum. That's better. My hunger is now " \
               f"{self.tamagotchi.hunger}."

    def feed_medicine(self):
        self.tamagotchi.health = 100
        return "Phewf! I feel so much better. My health is now at 100"

    def play_tamagotchi(self, activity):
        """
        Determines the happines value of the input activity and
        increases the tamgotchi's happiness by that value
        :param activity:
        :return: string telling user how much the tamagotchi's
        happiness increased
        """

        for element in self.act_list:
            if element.name == activity:
                chosen_act = element

        increase_value = \
            self.tamagotchi.increase_happiness(
                chosen_act.happiness_value)

        return f"Yay! My happiness is now {self.tamagotchi.happiness}."

