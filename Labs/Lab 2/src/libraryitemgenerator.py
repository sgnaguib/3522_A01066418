from dvd import DVD
from book import Book
from journal import Journal


class LibraryItemGenerator:
    """
    Provides users with a list of library items and takes input 
    for the information regarding the creation of a new item
    """

    @classmethod
    def create_dvd(cls):
        """
        Prompts user to create a dvd item
        :return: a dvd item
        """
        title = input("input dvd title\n")
        call_num = input("input dvd call number\n")
        num_copies = input("input number of copies\n")
        release_date = input("input release date\n")
        region_code = input("input region code\n")

        return DVD(title, call_num, int(num_copies), release_date,
                   region_code)

    @classmethod
    def create_book(cls):
        """
        Prompts user to create a book item
        :return: a book item
        """
        title = input("input book title\n")
        call_num = input("input book call number\n")
        num_copies = input("input number of copies\n")
        author = input("input author\n")

        return Book(title, call_num, int(num_copies), author)

    @classmethod
    def create_journal(cls):
        """
        Prompts user to create a dvd item
        :return: a dvd item
        """
        title = input("input journal title\n")
        call_num = input("input journal call number\n")
        num_copies = input("input number of copies\n")
        issue_num = input("input issue number\n")
        publisher = input("input publisher\n")

        return Journal(title, call_num, int(num_copies), issue_num,
                   publisher)

    @classmethod
    def gen_item(cls):
        """
        Prompts user to create a new library item
        :return: a newly created item
        """
        prompt = 'Please select an item type\n' \
                 '1.DVD\n' \
                 '2.book\n' \
                 '3.journal\n'
        user_input = input(prompt)

        while user_input not in ['1', '2', '3']:
            user_input = input('Invalid input\n' + prompt)

        method_dict = {1: cls.create_dvd, 2: cls.create_book,
                       3: cls.create_journal}

        return method_dict[int(user_input)]()

