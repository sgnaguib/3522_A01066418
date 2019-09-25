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
        print(self.game.check_status())
        print(self.game.get_message())
        self.main_menu()

    def food_menu(self):

        food_dict = {1: 'spaghetti', 2: 'cabbage', 3: 'baguette'}

        food_menu = "\nSelect a food:\n" \
                    "1. Spaghetti \n" \
                    "2. Cabbage \n" \
                    "3. Baguette\n" \
                    '4. Medicine\n'\
                    "5. To go back to main menu\n"

        food_choice = input(food_menu)

        while food_choice not in ['1', '2', '3', '4', '5']:
            food_choice = input("Invalid input. Try again.\n" +
                                food_menu)

        if food_choice == '5':  # exit option
            self.main_menu()

        elif food_choice == '4':  # medicine option
            print(self.game.feed_medicine())
            self.main_menu()

        else:
            print(self.game.feed_tamagotchi(food_dict.get(
                                    int(food_choice))))
            self.main_menu()

    def activity_menu(self):

        act_dict = {1: 'pillow fight', 2: 'staring contest',
                    3: 'monopoly'}

        act_menu = "\nSelect an activity:\n" \
                    "1. Pillow Fight \n" \
                    "2. Staring Contest \n" \
                    "3. Monopoly \n" \
                    "4. To go back to main menu\n"

        act_choice = input(act_menu)

        if act_choice == '4':  # exit option
            self.main_menu()

        while act_choice not in ['1', '2', '3']:
            act_choice = input("Invalid input. Try again.\n" +
                                act_menu)

        print(self.game.play_tamagotchi(act_dict.get(
            int(act_choice))))

    main_menu_dict = {1: tamagotchi_status, 2: food_menu,
                      3: activity_menu, 4: exit}


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

