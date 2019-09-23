import abc


class Food(abc.ABC):
    """
    Represents Tamagotchi food
    """

    def __init__(self, name, hunger_value):
        self.name = name
        self.hunger_value = hunger_value
