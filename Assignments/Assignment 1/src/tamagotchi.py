import abc


class Tamagotchi(abc):
    """
    Represents a tamagotchi - a virtual pet that the user is supposed
    to care for.
    """

    def __init__(self, health=100, happiness=100, hunger=0):
        self.health = health
        self.happiness = happiness
        self.hunger = hunger


    @abc.abstractmethod
    def tamagotchi_message(self):
        pass

