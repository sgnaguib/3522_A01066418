import tamagotchi


class Mussolini(tamagotchi.Tamagotchi):
    """
    Represents a mussolini tamagotchi
    """

    FRAGILITY = 2
    SICK_POINT = 50
    PLAYFULNESS = 10

    def __init__(self):
        super().__init__('Mussolini')
        self.preferred_food = ['spaghetti', 'cabbage']

    def message(self):
        """
        a getter method for this tamagotchi's message
        :return:  Mussolini's message, telling the user how happy
        (or not) he is.
        """
        if self.health < self.SICK_POINT:
            return "I'm sick :("
        if self.happiness > 50:
            return 'Dolce vida!'
        else:
            return 'Quel Miseria!'


