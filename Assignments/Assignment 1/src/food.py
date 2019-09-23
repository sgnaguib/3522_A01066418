import abc


class Food(abc):
    """
    Represents Tamagotchi food
    """
    @property
    @abc.abstractmethod
    def hunger_value(self):
        pass

    @property
    @abc.abstractmethod
    def name(self):
        pass
