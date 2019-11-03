"""
This module contains all the basic pizza class and all its possible
wrappers. A pizza has a price and a list of ingredients it contains.
"""


class Pizza:
    PRICE = 4.99

    def __init__(self):
        self.cost = self.PRICE
        self.ingredients = ['Signature Crust']


class ParmigianoPizza:
    PRICE = 4.99

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + self.PRICE
        self.ingredients = pizza.ingredients
        self.ingredients.append('Parmigiano Reggiano')


class MozzarellaPizza:
    PRICE = 3.99

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + self.PRICE
        self.ingredients = pizza.ingredients
        self.ingredients.append('Fresh Mozzarella')


class VeganCheesePizza:
    PRICE = 6.99

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + self.PRICE
        self.ingredients = pizza.ingredients
        self.ingredients.append('Vegan Cheese')


class PeppersPizza:
    PRICE = 1.50

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + self.PRICE
        self.ingredients = pizza.ingredients
        self.ingredients.append('Peppers')


class PineapplePizza:
    PRICE = 2.00

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + self.PRICE
        self.ingredients = pizza.ingredients
        self.ingredients.append('Pineapples')


class MushroomsPizza:
    PRICE = 1.50

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + self.PRICE
        self.ingredients = pizza.ingredients
        self.ingredients.append('Mushrooms')


class BasilPizza:
    PRICE = 2.00

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + self.PRICE
        self.ingredients = pizza.ingredients
        self.ingredients.append('Fresh Basil')


class SpinachPizza:
    PRICE = 1.00

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + self.PRICE
        self.ingredients = pizza.ingredients
        self.ingredients.append('Spinach')


class PepperoniPizza:
    PRICE = 3.00

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + self.PRICE
        self.ingredients = pizza.ingredients
        self.ingredients.append('Pepperoni')


class BeyondPizza:
    PRICE = 4.00

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + self.PRICE
        self.ingredients = pizza.ingredients
        self.ingredients.append('Beyond Meat')




