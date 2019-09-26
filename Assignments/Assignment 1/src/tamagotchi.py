import abc
import random


class Tamagotchi(abc.ABC):
    """
    Represents a tamagotchi - a virtual pet that the user is supposed
    to care for.
    """
    MAX = 100
    MIN = 0

    def __init__(self, name, health=100, happiness=100, hunger=0):
        self.name = name
        self._health = health
        self._happiness = happiness
        self._hunger = hunger

    @property
    @abc.abstractmethod
    def PLAYFULNESS(self):
        pass

    @property
    @abc.abstractmethod
    def FRAGILITY(self):
        pass

    def get_health(self):
        return self._health

    def set_health(self, new_health):
        if new_health < self.MIN:
            self._health = self.MIN
        else:
            self._health = new_health

    health = property(get_health, set_health)

    def get_happiness(self):
        return self._happiness

    def set_happiness(self, new_happiness):
        if new_happiness < self.MIN:
            self._happiness = self.MIN
        elif new_happiness > self.MAX:
            self._happiness = self.MAX
        else:
            self._happiness = new_happiness

    happiness = property(get_happiness, set_happiness)

    def get_hunger(self):
        return round(self._hunger)

    def set_hunger(self, new_hunger):
        if new_hunger < self.MIN:
            self._hunger = self.MIN
        elif new_hunger > self.MAX:
            self._hunger = self.MAX
        else:
            self._hunger = new_hunger

    hunger = property(get_hunger, set_hunger)

    @abc.abstractmethod
    def message(self, happiness_increase):
        pass

    def decrease_hunger(self, value):
        self.hunger -= value

    def check_status(self):
        return f"Hi! My name is {self.name}, my " \
               f"health is {self.health}, " \
               f"my happiness is {self.happiness}, " \
               f"and my hunger is {self.hunger}"

    def increase_happiness(self, value):
        increase_value = value - self.PLAYFULNESS
        self.happiness += increase_value
        return increase_value

    def update_status(self, time):
        self.hunger += time * self.FRAGILITY
        self.happiness -= time * self.FRAGILITY
        if self.hunger < self.MAX:
            self.health -= time * self.FRAGILITY
        else:
            self.health -= time * self.FRAGILITY * 2



