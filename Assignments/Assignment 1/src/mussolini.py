import tamagotchi


class Mussolini(tamagotchi.Tamagotchi):
    """
    Represents a mussolini tamagotchi
    """

    def __init__(self):
        super().__init__('Mussolini')
        self.preferred_food = 'spaghetti'

    def tamagotchi_message(self):
        """
        a getter method for this tamagotchi's message
        :return:  Mussolini's message, telling the user how happy
        (or not) he is.
        """
        if self.happiness > 50:
            return 'Dolce vida!'
        else:
            return 'Quel Miseria!'