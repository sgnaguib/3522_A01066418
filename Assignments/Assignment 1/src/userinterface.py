from game import Game


class UserInterface:
    """
    The text-based interface for the user to interact with the
    tamagotchi.
    """

    def __init__(self, game):
        self.game = game

    def main_menu(self):
        main_menu = "\nSelect an option:\n" \
            "1. Check your tamagotchi's status \n" \
            "2. Feed your tamagotchi \n" \
            "3. Play with your tamagotchi\n" \
            "4. To quit\n"
        return main_menu

    def print_tamagotchi_status(self):
        print('')


def main():
    """
    Driver to test implementation.
    """
    game = Game()
    ui = UserInterface(game)
    print("Welcome to your new game. A randomly selected tamgotchi "
          "has been created for you!")

    while 1:

        usr_input = input(ui.main_menu())

        while usr_input not in ['1', '2', '3', '4']:
            usr_input = input("Invalid input. Try again.\n" +
                              ui.main_menu())

        def option_one():
            print(game.tamagotchi.check_status())

        def option_two():
            main_menu = "\nSelect a food:\n" \
                        "1. Spaghetti \n" \
                        "2. Cabbage \n" \
                        "3. Baguette\n" \
                        "4. To go back to main menu\n"
            usr_input = input("Invalid input. Try again.\n" +
                              ui.print_main_menu())

        def option_three():
            print("")

        main_menu_dict = {1: option_one, 2: option_two, 3: option_three,
                          4: exit}

        main_menu_dict[int(usr_input)]()


if __name__ == '__main__':
    main()

