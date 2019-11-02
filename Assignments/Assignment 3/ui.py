from menu import Menu

class UI:

    def doNothing(self):
        pass

    def __init__(self):


        topping_options = [("Peppers    1.5", self.doNothing),
                           ("Pineapple   2", self.doNothing),
                           ("Check out  ", self.checkout)]

        self.topping_menu = Menu(
            options=topping_options,
            title="Step 2:",
            message="Select Your Toppings!")

        self.topping_menu.set_prompt(">")

        cheese_options = [("Parmigiano Reggiano", self.doNothing),
                          ("Select Toppings", self.topping_menu.open)]


        self.cheese_menu = Menu(
            options=cheese_options,
            title="Step 1:",
            message="Select Your Cheese!")


    def checkout(self):
        pass

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
