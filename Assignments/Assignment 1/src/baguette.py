import food


class Baguette(food.Food):
    """
    Represents a baguette, a type of tamagotchi food
    """

    def __init__(self):
        super().__init__('baguette', 25)

