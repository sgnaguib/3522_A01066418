from card import *


class CardManager:
    """
    Manages a list of a variety of different
    cards someone might carry in their wallet. Through the card manager,
    a user can add, search and delete cards. Stored cards can also
    be backed up a .txt file.
    """

    types = {'Bank Card': BankCard, 'Punch Card': PunchCard,
             'ID': IdCard, 'Membership Card': MembershipCard,
             'Gift Card': GiftCard, 'Personal Card': PersonalCard,
             'Business Card': BusinessCard}

    def __init__(self):
        self.wallet = []


    def add_card(self, card_type):

        self.wallet.append(self.types[card_type]("AN ID CARD"))
        print(self.wallet)



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




