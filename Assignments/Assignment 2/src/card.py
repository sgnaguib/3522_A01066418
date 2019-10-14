import abc
from inputhandler import dinput


class Card(abc.ABC):

    def __init__(self):
        self.name = input("Please input the name of your card"
                          " (i.e. Shopper's Membership Card)\n")

    def __str__(self):

        string = ""
        for element in self.__dict__:
            string += (f"{element.title().replace('_', ' ')}: "
                        f"{self.__dict__[element]}\n")
        return string


class IdCard(Card):

    def __init__(self):
        super().__init__()
        self.institution = input("Please input the name of card issuer\n")
        self.card_number = input("Please input the card number\n")
        self.issue_date = input("Please input the card expiry date\n")



class PunchCard(Card):

    def __init__(self):
        super().__init__()

class BankCard:
    def __init__(self):
        pass


class MembershipCard:
    def __init__(self):
        pass


class GiftCard:
    def __init__(self):
        pass


class PersonalCard:
    def __init__(self):
        pass


class PersonalCard:
    def __init__(self):
        pass


class BusinessCard:
    def __init__(self):
        pass

