from menu import Menu
from pizza import *
from prettytable import PrettyTable


class UI:

    cheese_dict = {'Parmigiano Reggiano': ParmigianoPizza,
                   'Fresh Mozzarella': MozzarellaPizza,
                   'Vegan Cheese': VeganCheesePizza}

    topping_dict = {'Peppers': PeppersPizza,
                   'Pineapple': PineapplePizza,
                   'Mushrooms': MushroomsPizza,
                   'Fresh Basil': BasilPizza,
                   'Spinach': SpinachPizza,
                   'Pepperoni':PepperoniPizza,
                   'Beyond Meat':BeyondPizza}

    def __init__(self):

        self.pizza = Pizza()

        topping_options = []
        for element in self.topping_dict.items():
            topping_options.append((element[0], self.add_topping,
                                   {'kind': element[1]}))
        topping_options.append(("Check Out", self.checkout()))


        self.topping_menu = Menu(
            options=topping_options,
            title="Step 2:",
            message="Select Your Toppings!")

        self.topping_menu.set_prompt(">")

        cheese_options = []
        for element in self.cheese_dict.items():
            cheese_options.append((element[0], self.add_cheese,
                                   {'kind': element[1]}))
        cheese_options.append(("Topping Menu", self.topping_menu.open))

        self.cheese_menu = Menu(
            options=cheese_options,
            title="Step 1:",
            refresh=lambda:
            self.cheese_menu.set_message("Choose Another Cheese Or "
                                         "Continue to Topping Menu"),
            message="Select Your Cheese!")

    def add_cheese(self, kind):
        self.pizza = kind(self.pizza)
        print("Cheese successfully added")
        self.print_ingredients()

    def add_topping(self, kind):
        self.pizza = kind(self.pizza)
        print("Topping successfully added")
        self.print_ingredients()

    def print_ingredients(self):
        print("So far, your pizza contains the following:")
        for ingredient in self.pizza.ingredients:
            print(f"{ingredient}")
        print("\n")

    def checkout(self):
        print("Here is your bill:\n")
        bill = PrettyTable(['Ingredient', 'Cost'])
        for ingredient in self.pizza.ingredients:
            bill.add_row([ingredient, self.get_cost(ingredient)])
        bill.add_row(['Total', self.pizza.cost])
        print(bill)
        input("Press Enter to Exit Program")
        quit()

    def get_cost(self, ingredient):

        prices = {'Signature Crust': 4.99, 'Parmigiano Reggiano': 4.99}
        return prices[ingredient]

    def run(self):

        print("Welcome to the Python Pizza Company. \nWhere we"
              " let you build your own custom dream pizza.")
        print("All are pizzas are assembled on our signature crust "
              "and start off at $4.99.\nWhen you are "
              "ready to select your cheese and topping, press Enter")
        input()
        self.cheese_menu.open()


def main():
    ui = UI()
    ui.run()


if __name__ == '__main__':
    main()
