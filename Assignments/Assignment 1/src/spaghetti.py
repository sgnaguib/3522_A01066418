import food


class Spaghetti(food.Food):
    """
    Represents spaghetti, a type of tamagotchi food
    """

    def __init__(self):
        super().__init__('spaghetti', 30)

