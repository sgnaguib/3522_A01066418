import abc


class Activity(abc.ABC):
    """
    Represents an activity for a user to do with a tamagotchi
    """

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def play(self):
        pass
