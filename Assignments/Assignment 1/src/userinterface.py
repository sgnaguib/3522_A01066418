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

        usr_input = input(main_menu)

        while usr_input not in ['1', '2', '3', '4']:
            usr_input = input("Invalid input. Try again.\n" +
                              main_menu)

        choice = self.main_menu_dict[int(usr_input)]
        choice(self) # why do we need to pass it self?

    def tamagotchi_status(self):
        # Checking tamagotchi status
        print(self.game.tamagotchi.check_status())
        self.main_menu()

    def food_menu(self):

        food_dict = {1: 'spaghetti', 2: 'cabbage', 3: 'baguette'}

        food_menu = "\nSelect a food:\n" \
                    "1. Spaghetti \n" \
                    "2. Cabbage \n" \
                    "3. Baguette\n" \
                    "4. To go back to main menu\n"

        while 1:

            food_choice = input(food_menu)

            if food_choice == '4':  # exit option
                self.main_menu()

            while food_choice not in ['1', '2', '3']:
                food_choice = input("Invalid input. Try again.\n" +
                                    food_menu)

            print(self.game.feed_tamagotchi(food_dict.get(
                                            int(food_choice))))

    main_menu_dict = {1: tamagotchi_status, 2: food_menu,
                      3: 'nothing', 4: exit}


def main():
    """
    Driver.
    """
    game = Game()
    ui = UserInterface(game)
    print("Welcome to your new game. A randomly selected tamgotchi "
          "has been created for you!")
    ui.main_menu()

if __name__ == '__main__':
    main()

