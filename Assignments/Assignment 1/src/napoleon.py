import tamagotchi


class Napoleon(tamagotchi.Tamagotchi):
    """
    Represents a Napoleon tamagotchi
    """

    def __init__(self, health, happiness, hunger):
        super().__init__(health, happiness, hunger)
        self.preferred_food = 'baguette'
        self.name = 'Napoleon'

    def tamagotchi_message(self):
        """
        a getter method for this tamagotchi's message
        :return:  Mussolini's message, telling the user how happy
        (or not) he is.
        """
        if self.happiness > 50:
            return 'La vie est belle!'
        else:
            return "C'est la merde!"
