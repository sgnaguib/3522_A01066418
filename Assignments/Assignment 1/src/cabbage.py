import food


class Cabbage(food.Food):
    """
    Represents cabbage, a type of tamagotchi food
    """

    def __init__(self):
        super().__init__('cabbage', 20)

