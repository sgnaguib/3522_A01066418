from menu import Menu
from cardmanager import CardManager
from card import CardEnum


class UI:
    """
    Represents the text-based UI for a card manager.
    """
    def __init__(self, manager):
        """
        Initializes all the menu options of the UI
        :param manager:
        """
        self.manager = manager

        view_options = [("Main Menu", Menu.CLOSE)]

        self.view_cards = Menu(
            options=view_options,
            title="Your Cards",
            message="Select 1 to return to the main menu "
                    "or select your card to view its information",
            refresh=self.list_cards)

        add_options = self.get_card_options()

        self.add_menu = Menu(
            options=add_options,
            title="Add Menu",
            message="Select What Type of Card You'd like to Add")

        mm_options = [("View cards", self.view_cards.open),
                      ("Add a card", self.add_menu.open),
                      ("Search for a card", self.search_card),
                      ("Delete a card", self.delete_card),
                      ("Back up data", self.back_up),
                      ("Exit program", self.goodbye)]

        self.main_menu = Menu(
            options=mm_options,
            title="Main Menu",
            message="Welcome to iWallet, please select an option")
        self.main_menu.set_prompt(">")

    def get_card_options(self):
        """
        Go through all the CardEnum members, and generates
        a tuple the UI can use to display the Card Types as
        options for the user to select
        :return: tuple of Card Types
        """
        cards_list = []

        for card in CardEnum:
            card_tuple = (card.value, self.add_card,
                          {'card_type': card.value})
            cards_list.append(card_tuple)
        cards_list.append(("Main Menu", Menu.CLOSE))

        return cards_list

    def add_card(self, card_type):
        """Gets all the attributes associated with a particular
        card type and prompts the user to input information for
        these of the attributes"""
        card = self.manager.get_card(card_type)
        new_dict = card.__dict__
        for attribute in card.__dict__:
            new_dict[attribute] = \
                input(f"Please input {attribute.replace('_', ' ')}:\n")

        self.manager.add_card(card_type, **new_dict)

        print(f"Card succesfully added\n")
        input("Press Enter to return to the add menu...\n")

    def list_cards(self):
        """Generates the menu list of all the card's currently
        being stored"""
        view_options = [("Main Menu", Menu.CLOSE)]
        for card in self.manager.cards:
            view_options.append((card.card_name, self.print_card,
                                        {'card': card}))
        self.view_cards.options = view_options

    @staticmethod
    def print_card(card):
        print("Card Details:\n")
        print(str(card))
        input("Press Enter to return to main menu...\n")

    def search_card(self):
        card_name = input("Please input the name of the card"
                          " you'd like to find\n")

        card = self.manager.search_card(card_name)

        if card is not None:
            print(f"\nWe found your card. Here is its information:\n"
                  f"{str(card)}")
        else:
            print(f"Sorry - there is no card by that name\n")

        input("Press Enter to return to main menu...\n")

    def delete_card(self):
        card_name = input("Please input the name of the card"
                          " you'd like to delete\n")

        deleted = self.manager.delete_card(card_name)

        if deleted:
            print(f"\nYour Card Was Successfully Deleted\n")
        else:
            print(f"Sorry - there is no card by that name\n")

        input("Press Enter to return to main menu...\n")

    def back_up(self):
        self.manager.export_cards()

    @staticmethod
    def goodbye():
        """
        Deals with a user who wants to exit the game
        """
        print("\nThanks for using iWallet. Goodbye!")
        quit()

    def run(self):
        self.main_menu.open()


def main():
    manager = CardManager()
    ui = UI(manager)
    ui.run()


if __name__ == "__main__":
    main()