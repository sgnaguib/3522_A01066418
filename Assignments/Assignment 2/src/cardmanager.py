from card import *


class CardManager:
    """
    Manages a list of a variety of different
    cards someone might carry in their wallet. Through the card manager,
    a user can add, search and delete cards. Stored cards can also
    be backed up a .txt file.
    """

    types = {'Bank Card': BankCard, 'Punch Card': PunchCard,
             'ID Card': IdCard, 'Membership Card': MembershipCard,
             'Gift Card': GiftCard, 'Personal Card': PersonalCard,
             'Business Card': BusinessCard}

    def __init__(self):
        self.cards = []

    def add_card(self, card_type):

        self.cards.append(self.types[card_type]())

    def search_card(self):
        pass

    def delete_card(self):
        pass

    def export_cards(self):
        pass





