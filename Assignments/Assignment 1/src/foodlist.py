from food import Food


class FoodList:
    """
    List of all food used in the tamagotchi game
    """

    def __init__(self):
        cabbage = Food('cabbage')
        spaghetti = Food('spaghetti')
        baguette = Food('baguette')
        self.food_list = [cabbage, spaghetti, baguette]

    def get_food_list(self):
        return self.food_list
