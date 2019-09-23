import tamagotchi


class Stalin(tamagotchi.Tamagotchi):
    """
    Represents a Stalin tamagotchi
    """

    def __init__(self):
        super().__init__('Stalin')
        self.preferred_food = 'cabbage'

    def tamagotchi_message(self):
        """
        a getter method for this tamagotchi's message
        :return:  Stalin's message, telling the user how happy
        (or not) he is.
        """
        if self.happiness > 50:
            return 'My mustache is happy'
        else:
            return 'My mustache is sad'
