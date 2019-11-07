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

    @abc.abstractmethod
    def create_item(self) -> Item:
        pass


class BookFactory(ItemFactory):
    """
    The GuestFactory is responsible for creating Guests USer Accounts.
    """

    def create_item(self) -> Book:
        title = input("input book title\n")
        call_num = input("input book call number\n")
        num_copies = input("input number of copies\n")
        author = input("input author\n")

        return Book(title, call_num, int(num_copies), author)


class JournalFactory(ItemFactory):
    """
    The JournalFactory is responsible for creating Journal Items
    """

    def create_item(self) -> Journal:
        title = input("input journal title\n")
        call_num = input("input journal call number\n")
        num_copies = input("input number of copies\n")
        issue_num = input("input issue number\n")
        publisher = input("input publisher\n")

        return Journal(title, call_num, int(num_copies), issue_num,
                       publisher)


class DVDFactory(ItemFactory):
    """
    The JournalFactory is responsible for creating Journal Items
    """
    def create_item(self) -> DVD:
        title = input("input dvd title\n")
        call_num = input("input dvd call number\n")
        num_copies = input("input number of copies\n")
        release_date = input("input release date\n")
        region_code = input("input region code\n")

        return DVD(title, call_num, int(num_copies), release_date,
                   region_code)

