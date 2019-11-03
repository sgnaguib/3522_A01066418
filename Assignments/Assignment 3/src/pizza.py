class Pizza:

    def __init__(self):
        self._cost = 4.99
        self._ingredients = ['Signature Crust']

    @property
    def cost(self):
        return self._cost

    @property
    def ingredients(self):
        return self._ingredients


class ParmigianoPizza:

    def __init__(self, pizza):
        self.pizza = pizza

    @property
    def cost(self):
        return self.pizza.cost + 4.99

    @property
    def ingredients(self):
        return self.ingredients.append('Parmigiano Reggiano')