import tamagotchi


class Napoleon(tamagotchi.Tamagotchi):
    """
    Represents a Napoleon tamagotchi
    """

    FRAGILITY = 4
    PLAYFULNESS = 0
    SICK_POINT = 60

    def __init__(self):
        super().__init__('Napoleon')
        self.preferred_food = ['baguette', 'spaghetti']

    def message(self):
        """
        a getter method for this tamagotchi's message
        :return:  Mussolini's message, telling the user how happy
        (or not) he is.
        """
        if self.happiness > 50:
            return 'La vie est belle!'
        else:
            return "C'est la merde!"

