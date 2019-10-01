
class UI:
    """
    The text-based interface for the user to interact with the
    cardmanager.
    """

    def main_menu(self):

        main_menu = "\nSelect an option:\n" \
                "1. Add a card \n" \
                "2. Search for a card \n" \
                "3. Delete a card\n" \
                "4. Back up your cards\n" \
                "5. Exit\n"

        usr_input = input(main_menu)

        while usr_input not in ['1', '2', '3', '4', '5']:
            usr_input = input("Invalid input. Try again.\n" +
                              main_menu)

        return int(usr_input)
