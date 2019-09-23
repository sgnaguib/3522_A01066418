import abc
import random


class Tamagotchi(abc.ABC):
    """
    Represents a tamagotchi - a virtual pet that the user is supposed
    to care for.
    """

    def __init__(self, name, health=100, happiness=100, hunger=0):
        self.name = name
        self.health = health
        self.happiness = happiness
        self.hunger = hunger

    # @abc.abstractmethod
    # def tamagotchi_message(self):
    #     pass


    def decrease_hunger(self, value):
        self.hunger -= value

    def check_status(self):
        return f"Hi! My name is {self.name}, my " \
               f"health is {self.health}, " \
               f"my happiness is {self.happiness}, " \
               f"and my hunger is {self.hunger}"



