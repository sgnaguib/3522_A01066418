import tamagotchi

class mussolini(tamagotchi):
    """
    Represents a mussolini tamagotchi
    """

    def __init__(self, health, happiness, hunger):
        super().__init__(health, happiness, hunger)
        self.preferred_food = 'spaghetti'
