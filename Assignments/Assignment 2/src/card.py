import abc

class Card(abc.ABC):

    def __init__(self, name):
        self.name = name


class IdCard(Card):

    def __init__(self, name):
        super().__init__(name)


class PunchCard(Card):

    def __init__(self, name):
        super().__init__(name)

class BankCard:
    def __init__(self, name):
        super().__init__(name)


class MembershipCard:
    def __init__(self, name):
        super().__init__(name)


class GiftCard:
    def __init__(self, name):
        super().__init__(name)


class PersonalCard:
    def __init__(self, name):
        super().__init__(name)

class PersonalCard:
    def __init__(self, name):
        super().__init__(name)

