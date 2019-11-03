class Pizza:

    def __init__(self):
        self.cost = 4.99
        self.ingredients = ['Signature Crust']


class ParmigianoPizza:

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + 4.99
        self.ingredients = pizza.ingredients
        self.ingredients.append('Parmigiano Reggiano')


class MozzarellaPizza:

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + 3.99
        self.ingredients = pizza.ingredients
        self.ingredients.append('Fresh Mozzarella')

class VeganCheesePizza:

    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + 5.99
        self.ingredients = pizza.ingredients
        self.ingredients.append('Vegan Cheese')

class PeppersPizza:
    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + 1.50
        self.ingredients = pizza.ingredients
        self.ingredients.append('Peppers')


class PineapplePizza:
    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + 2
        self.ingredients = pizza.ingredients
        self.ingredients.append('Pineapples')


class MushroomsPizza:
    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + 1.50
        self.ingredients = pizza.ingredients
        self.ingredients.append('Mushrooms')


class BasilPizza:
    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + 2
        self.ingredients = pizza.ingredients
        self.ingredients.append('Fresh Basil')


class SpinachPizza:
    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + 1
        self.ingredients = pizza.ingredients
        self.ingredients.append('Spinach')


class PepperoniPizza:
    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + 3
        self.ingredients = pizza.ingredients
        self.ingredients.append('Pepperoni')


class BeyondPizza:
    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = pizza.cost + 4
        self.ingredients = pizza.ingredients
        self.ingredients.append('Beyond Meat')




