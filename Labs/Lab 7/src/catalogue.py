from libraryitemgenerator import LibraryItemGenerator


class Catalogue:
    """
    Represents a list of items stored in a library
    """

    def __init__(self):
        """
        Creates a new catalogue with an empty list of items
        """
        self._item_list = []

        self.item_list = property()

    def find_item(self, title):
        """
        Search the library's list of items for a title. If the list
        contains the title, return the item
        :param title: title of a item
        :return: the item that matches title from parameter
        """

        for element in self.item_list:
            if element.title == title:
                return element

        print("item could not be found")

    def add_item(self):
        """
        Adds a item to the library's collection if the collection
        doesn't already contain the item
        """
        item = LibraryItemGenerator.gen_item()

        if item not in self.item_list:
            self.item_list.append(item)

    def remove_item(self, call_number):
        """
        Removes a item from the library's item collection
        :param call_number: A item's call number
        :return: Message telling user whether item was successfully
        deleted
        """
        for element in self.item_list:
            if element.call_number == call_number:
                self.item_list.remove(element)
                return "item successfully removed"
        return "item could not be found"

    def check_out(self, call_number):
        """
        Checks a item out from the library if it exists.
        Every time a item is checked out, the number of copies available
        of the item is decremented by 1.
        :param call_number: A item's call number
        :return: Message telling user whether the check out was
        successful
        """
        for element in self.item_list:
            if element.call_number == call_number:
                if element.num_copies <= 0:
                    return "No copies available"
                element.num_copies -= 1
                return "item successfully checked-out"
        return "item could not be found"

    def return_item(self, call_number):
        """
        Returns a item to the library's collection if the item exists
        in the collection. Once a item is returned, its number of copies
         available is incremented by 1
        :param call_number: a item's call number
        :return: Message telling user whether the return was successful
        """
        for element in self.item_list:
            if element.call_number == call_number:
                element.num_copies += 1
                return "item successfully returned"
        return "item could not be found"


