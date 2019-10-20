from card import *
from pathlib import Path
import arrow

class CardManager:
    """
    Manages a list of a variety of different
    cards someone might carry in their wallet. Through the card manager,
    a user can add, search and delete cards. Stored cards can also
    be backed up a .txt file.
    """

    types = {'Bank Card': BankCard, 'Punch Card': PunchCard,
             'School Card': SchoolCard, 'Government ID': GovID,
             'Membership Card': MembershipCard,
             'Gift Card': GiftCard, 'Personal Card': PersonalCard,
             'Business Card': BusinessCard}


    def __init__(self):
        self.cards = []

    def add_card(self, card_type, **kwargs):
        new_card = self.types[card_type](**kwargs)
        self.cards.append(new_card)
        print(new_card)
        # replace args with dictionary
        #
        #     new_card = self.types[card_type](*args)
        # self.types[card_type].generate_card()
        #     print(new_card)
            #self.cards.append(new_card)

    def get_card(self, card_type):
        return self.types[card_type]()

    def search_card(self, card_name):
        for card in self.cards:
            if card.card_name == card_name:
                return card
        return None

    def delete_card(self, card_name):
        for card in self.cards:
            if card.card_name == card_name:
                return True
        return False

    def export_cards(self):
        day = arrow.now().format('DDMMYY')
        time = arrow.now().format('HHMM')
        file_name = (f'iWallet_Export_{day}_{time}.txt')
        path = Path.cwd()/file_name
        with open(path, mode='w', encoding='utf-8') as the_file:
            for card in self.cards:
                the_file.write(f"{card.export_format()}\n")
        the_file.close()






