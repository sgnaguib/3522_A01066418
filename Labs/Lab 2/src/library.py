from catalogue import Catalogue
from book import Book


class Library:
    """
    Represent a library that has a collection of items.
    The library can create, search, check out and return items.
    """

    def __init__(self):
        """
        Creates a new library with an empty list of items
        """
        self.myCatalogue = Catalogue()

    def add_item(self):
        """
        Adds a book to the library's collection if the collection
        doesn't already contain the book
        """
        self.myCatalogue.add_item()

    def remove_item(self, call_number):
        """
        Removes a book from the library's book collection
        :param call_number: A book's call number
        :return: Message telling user whether book was successfully
        deleted
        """
        return self.myCatalogue.check_out(call_number)

    def check_out(self, call_number):
        """
        Checks a book out from the library if it exists.
        Everytime a book is checked out, the number of copies available
        of the book is decremented by 1.
        :param call_number: A book's call number
        :return: Message telling user whether the check out was
        successful
        """
        return self.myCatalogue.check_out(call_number)

    def return_item(self, call_number):
        """
        Returns a book to the library's collection if the book exists
        in the collection. Once a book is returned, its number of copies
         available is incremented by 1
        :param call_number: a book's call number
        :return: Message telling user whether the return was successful
        """
        return self.myCatalogue.return_item(call_number)

    def find_item(self, title):
        """
        Search the library's list of items for a title. If the list
        contains the title, return the item
        :param title: title of a item
        :return: the item that matches title from parameter
        """
        return self.myCatalogue.find_item(title)

    def display_available_items(self):
        """
        Prints out the list of available items and their details
        """
        return self.myCatalogue.display_available_items()


def main():
    """
    Driver to test implementation.
    """
    vpl = Library()

    while 1:
        prompt = '\nSelect an option:\n' \
            '1. Remove item by call number \n' \
            '2. Check out item by call number\n' \
            '3. Return item by call number\n'\
            '4. Search for item by title\n'\
            '5. Display library catalogue\n'\
            '6. Add item to catalogue\n'\
            '7. To exit\n'

        usr_input = input(prompt)

        while usr_input not in ['1', '2', '3', '4', '5', '6', '7']:
            usr_input = input("Invalid input. Try again.\n" + prompt)

        def option_one():
            next_input = input('Input item\'s call number\n')
            print(vpl.remove_item(next_input))

        def option_two():
            next_input = input('Input item\'s call number\n')
            print(vpl.check_out(next_input))

        def option_three():
            next_input = input('Input item\'s call number\n')
            print(vpl.return_item(next_input))

        def option_four():
            next_input = input('Input item\'s title\n')
            print(vpl.find_item(next_input))

        method_dict = {1: option_one, 2: option_two, 3: option_three,
                       4: option_four,
                       5: vpl.display_available_items, 6: vpl.add_item,
                       7: exit}

        method_dict[int(usr_input)]()


if __name__ == '__main__':
    main()




