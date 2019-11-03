from menu import Menu
from pizza import *
from prettytable import PrettyTable


class UI:

    def doNothing(self):
        pass

    def __init__(self):

        self.pizza = Pizza()

        topping_options = [("Peppers    1.5", self.doNothing),
                           ("Pineapple   2", self.doNothing),
                           ("Check out  ", self.checkout)]

        self.topping_menu = Menu(
            options=topping_options,
            title="Step 2:",
            message="Select Your Toppings!")

        self.topping_menu.set_prompt(">")

        cheese_options = [("Parmigiano Reggiano", self.add_cheese),
                          ("Select Toppings", self.topping_menu.open)]

        self.cheese_menu = Menu(
            options=cheese_options,
            title="Step 1:",
            message="Select Your Cheese!")

    def add_cheese(self):
        self.pizza = ParmigianoPizza(self.pizza)
        print("Cheese successfully added")
        self.print_ingredients()

    def print_ingredients(self):
        print("So far, your pizza contains the following:\n")
        for ingredient in self.pizza.ingredients:
            print(f"{ingredient}\n")

    def checkout(self):
        print("Here is your a breakdown of your bill:\n")
        bill = PrettyTable(['Ingredient', 'Cost'])

    def run(self):

        print("Welcome to the Python Pizza Company. \nWhere we"
              " let you build your own custom dream pizza.")
        print("All are pizzas are assembled on our signature crust\n"
              "and start off at $4.99.\nWhen you are "
              "ready to select your cheese and topping, press Enter")
        input()
        self.cheese_menu.open()


def main():
    ui = UI()
    ui.run()


if __name__ == '__main__':
    main()
