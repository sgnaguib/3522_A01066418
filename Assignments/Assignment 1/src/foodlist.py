from food import Food


class FoodList:

    def __init__(self):
        cabbage = Food('cabbage')
        spaghetti = Food('spaghetti')
        baguette = Food('baguette')
        self.food_list = [cabbage, spaghetti, baguette]

    def get_food_list(self):
        return self.food_list
