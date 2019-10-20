from enum import Enum


class Card:
    """
    Represents a general card found in a wallet. Stores the information
    found on such a card.
    """

    def __init__(self, card_name="", **kwargs):
        """For a card's attribute, the first value in the
        array is the value of user inputs and """
        self.card_name = card_name

    def __str__(self):
        """
        Displays the card's information, one line for each of the
        card's attributes
        :return: formatted string
        """

        string = ""
        for element in self.__dict__:
            string += (f"{element.title().replace('_', ' ')}: "
                        f"{self.__dict__[element]}\n")
        return string

    def export_format(self):
        """
        Formats the cards information so it fits on one file.
        :return: formatted string
        """

        string = ""
        first = True
        for element in self.__dict__:
            details = (f"{element.title().replace('_', ' ')}: "
                            f"{self.__dict__[element]}")
            if first:
                string += details
                first = False
            else:
                string += f", {details}"

        return string


class InstitutionCard(Card):
    def __init__(self, cardholder_name="", card_number="",
                 issue_date="", expiry_date="", **kwargs):
        super().__init__(**kwargs)
        self.cardholder_name = cardholder_name
        self.card_number = card_number
        self.issue_date = issue_date
        self.expiry_date = expiry_date


class ContactCard(Card):
    def __init__(self, telephone_number="", email="",
                 address="", **kwargs):
        super().__init__(**kwargs)
        self.telephone_number = telephone_number
        self.email = email
        self.address = address


class GiftCard(Card):
    def __init__(self, business_name="", card_number="", expiry_date="",
                 **kwargs):
        super().__init__(**kwargs)
        self.business_name = business_name
        self.card_number = card_number
        self.expiry_date = expiry_date


class PunchCard(Card):
    def __init__(self, business_name="",
                 punches_available="", punches_claimed="", **kwargs):
        super().__init__(**kwargs)
        self.business_name = business_name
        self.punches_available = punches_available
        self.punches_claimed = punches_claimed


class BankCard(InstitutionCard):
    def __init__(self, name_of_bank="", **kwargs):

        super().__init__(**kwargs)
        self.name_of_bank = name_of_bank


class SchoolCard(InstitutionCard):
    def __init__(self, name_of_school="", **kwargs):
        super().__init__(**kwargs)
        self.name_of_school= name_of_school


class GovID(InstitutionCard):
    def __init__(self, name_of_government_department="", **kwargs):
        super().__init__(**kwargs)
        self.name_of_government_department = \
            name_of_government_department


class MembershipCard(InstitutionCard):
    def __init__(self, name_of_business="", **kwargs):
        super().__init__(**kwargs)
        self.name_of_business = name_of_business


class PersonalCard(ContactCard):
    def __init__(self, name_of_contact="",
                 title="", institution="", **kwargs):
        super().__init__(**kwargs)
        self.name_of_contact = name_of_contact
        self.title = title
        self.institution = institution


class BusinessCard(ContactCard):
    def __init__(self, name_of_business="", **kwargs):
        super().__init__(**kwargs)
        self.name_of_business = name_of_business


class CardEnum(Enum):
    """Contains all the different types of cards accepted
    defined above"""
    BANK_CARD = "Bank Card"
    PUNCH_CARD = "Punch Card"
    SCHOOL_CARD = "School Card"
    GOVID = "Government ID"
    MEMBERSHIP_CARD = "Membership Card"
    GIFT_CARD = "Gift Card"
    PERSONAL_CARD = "Personal Card"
    BUSINESS_CARD = "Business Card"

