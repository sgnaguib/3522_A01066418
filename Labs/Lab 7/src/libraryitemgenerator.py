from dvd import DVD
from book import Book
from journal import Journal
from item import Item
import abc


class LibraryItemGenerator:
    """
    takes input for the information regarding the creation of a new item
    """

    @classmethod
    def gen_item(cls, kind):
        """
        Prompts user to create a new library item
        :return: a newly created item
        """

        choice_factory_mapping = {
            'Journal': JournalFactory,
            'DVD': DVDFactory,
            'Book': BookFactory
        }

        factory = choice_factory_mapping[kind]()
        return factory.create_item()


class ItemFactory(abc.ABC):
    """
    The UserFactory class is the base class that the rest of the system
    depends on. It defines a factory interface that creates a user.
    """

    def get_input(self):
        title = input("input title\n")
        call_num = input("input call number\n")
        not_integer = True
        while not_integer:
            try:
                num_copies = int(input("input number of copies\n"))
            except ValueError:
                print("Error! You must enter an integer")
            else:
                not_integer = False

        return {'title': title,
                'call_num': call_num, 'num_copies': num_copies}

    @abc.abstractmethod
    def create_item(self) -> Item:
        pass


class BookFactory(ItemFactory):
    """
    The GuestFactory is responsible for creating Guests USer Accounts.
    """

    def create_item(self) -> Book:
        author = input("input author\n")
        kwargs = self.get_input()

        return Book(author, **kwargs)


class JournalFactory(ItemFactory):
    """
    The JournalFactory is responsible for creating Journal Items
    """

    def create_item(self) -> Journal:
        kwargs = self.get_input()
        issue_num = input("input issue number\n")
        publisher = input("input publisher\n")

        return Journal(issue_num,
                       publisher, **kwargs)


class DVDFactory(ItemFactory):
    """
    The JournalFactory is responsible for creating Journal Items
    """
    def create_item(self) -> DVD:
        kwargs = self.get_input()
        release_date = input("input release date\n")
        region_code = input("input region code\n")

        return DVD(release_date,
                   region_code, **kwargs)

