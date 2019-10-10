from example import UI

class CardManager:
    """
    Manages a list of a variety of different
    cards someone might carry in their wallet. Through the card manager,
    a user can add, search and delete cards. Stored cards can also
    be backed up a .txt file.
    """

    def __init__(self, ui):
        self.wallet = []
        self.ui = ui

    def add_card(self):
        print("poop")
        self.ui.add_card_menu()

    def search_card(self):
        pass

    def delete_card(self):
        pass

    def export_cards(self):
        pass

    def leave(self):
        """
        Exits the program
         """
        print("\nThanks for using e-wallet. Goodbye!")
        quit()

    def main_menu(self):
        choice = self.ui.main_menu()
        self.main_menu_dict.get(choice)(self) # why this again?

    main_menu_dict = {1: add_card, 2: search_card,
                      3: delete_card, 4: export_cards,
                      5: leave}


def main():
    UI.start()
    # wallet = CardManager()
    # wallet.main_menu()


if __name__ == '__main__':
    main()

