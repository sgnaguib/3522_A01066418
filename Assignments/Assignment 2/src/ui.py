from menu import Menu
from cardmanager import CardManager


class UI:

    def __init__(self, manager):
        self.manager = manager

        view_options = [("Main Menu", Menu.CLOSE)]

        self.view_cards = Menu(
            options=view_options,
            title="Your Cards",
            message="Select 1 to return to the main menu "
                    "or select your card to view its information",
            refresh=self.get_cards)

        business_options = [("Personal Business Card", self.add_card,
                             {'card_type': 'Personal Card'}),
                            ("Corporate Business Card", self.add_card,
                             {'card_type': 'Business'}),
                            ("Go Back", Menu.CLOSE)]

        self.business_menu = Menu(
            options=business_options,
            title="Add Menu",
            message="Please select the type of business card you'd "
                    "like to add")

        add_options = [("Bank card", self.add_card,
                        {'card_type': 'Bank Card'}),
                       ("Punch Card", self.add_card,
                        {'card_type': 'Punch Card'}),
                       ("ID Card", self.add_card,
                        {'card_type': 'ID Card'}),
                       ("Membership Card", self.add_card,
                        {'card_type': 'Membership Card'}),
                       ("Gift Card", self.add_card,
                        {'card_type': 'Gift Card'}),
                       ("Business Card", self.business_menu.open),
                       ("Main Menu", Menu.CLOSE)]

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

    def add_card(self, card_type):
        self.manager.add_card(card_type)

    def get_cards(self):
        view_options = [("Main Menu", Menu.CLOSE)]
        for card in self.manager.cards:
            view_options.append((card.name, self.print_card,
                                        {'card': card}))
        self.view_cards.options = view_options


    def print_card(self, card):
        print("Card Details:\n")
        print(str(card))

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

    def goodbye(self):
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