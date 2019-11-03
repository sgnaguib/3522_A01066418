from menu import Menu
from pizza import *
from prettytable import PrettyTable


class UI:

    cheese_dict = {'Parmigiano Reggiano': ParmigianoPizza,
                   'Fresh Mozzarella': MozzarellaPizza,
                   'Vegan Cheese': VeganCheesePizza}

    topping_dict = {'Peppers': PeppersPizza,
                   'Pineapples': PineapplePizza,
                   'Mushrooms': MushroomsPizza,
                   'Fresh Basil': BasilPizza,
                   'Spinach': SpinachPizza,
                   'Pepperoni':PepperoniPizza,
                   'Beyond Meat':BeyondPizza}

    ingredient_dict = {**cheese_dict, **topping_dict,
                       'Signature Crust': Pizza}

    def __init__(self):

        self.pizza = Pizza()

        topping_options = []
        for element in self.topping_dict.items():
            topping_options.append((f"{element[0]} | "
                                    f"${element[1].PRICE}",
                                    self.add_topping,
                                   {'kind': element[1]}))
        topping_options.append(("Check Out", self.checkout))

        self.topping_menu = Menu(
            options=topping_options,
            title="Step 2:",
            message="Choose a Topping Or Continue to Check Out!")

        self.topping_menu.set_prompt(">")

        cheese_options = []
        for element in self.cheese_dict.items():
            cheese_options.append((f"{element[0]} | "
                                   f"${element[1].PRICE}",
                                   self.add_cheese,
                                   {'kind': element[1]}))
        cheese_options.append(("Topping Menu", self.topping_menu.open))

        self.cheese_menu = Menu(
            options=cheese_options,
            title="Step 1:",
            message="Choose a Cheese Or Continue To Toppings")

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
            bill.add_row([ingredient,
                          self.ingredient_dict[ingredient].PRICE])
        bill.add_row(['Total', self.pizza.cost])
        print(bill)
        input("Press Enter to Exit Program")
        quit()


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
