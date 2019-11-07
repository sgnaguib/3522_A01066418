from catalogue import Catalogue
from menu import Menu


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

    def get_available_items(self):
        """
        Prints out the list of available items and their details
        """
        return self.myCatalogue.item_list()


class UI:

    def __init__(self, library):

        self.library = library

        mm_options = [("Remove item by call number", self.remove_item),
                      ("Check out item by call number", self.check_out),
                      ("Return item by call number", self.search_item),
                      ("Search for item by title", self.find_item),
                      ("Display library catalogue", self.display_items),
                      ("Add item to catalogue", self.add_item),
                      ("Exit Program", self.goodbye)]

        self.main_menu = Menu(
            options=mm_options,
            title="Main Menu",
            message="Welcome to iLibrary, please select an option")
        self.main_menu.set_prompt(">")

    def remove_item(self):
        next_input = input('Input item\'s call number\n')
        print(self.library.remove_item(next_input))

    def check_out(self):
        next_input = input('Input item\'s call number\n')
        print(self.library.check_out(next_input))

    def search_item(self):
        next_input = input('Input item\'s call number\n')
        print(self.library.return_item(next_input))

    def find_item(self):
        next_input = input('Input item\'s title\n')
        print(self.library.find_item(next_input))

    def display_items(self):
        item_list = self.library.get_available_items()
        for item in item_list:
            print(item)

    def add_item(self):
        self.library.add_item()

    @staticmethod
    def goodbye():
        """
        Deals with a user who wants to exit the game
        """
        print("\nThanks for using iWallet. Goodbye!")
        quit()

    def run(self):
        self.main_menu.open()


def main():
    """
    Driver to test implementation.
    """
    vpl = Library()

    ui = UI(vpl)

    ui.run()


if __name__ == '__main__':
    main()




