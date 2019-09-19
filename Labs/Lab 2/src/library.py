from book import Book

class Library:
    """
    Represent a library that has a collection of books.
    The library can search, check out and return books.
    """

    def __init__(self):
        """
        Creates a new library with an empty list of books
        """
        self.book_list = []

    def find_books(self, title):
        """
        Search the library's list of books for a title. If the list
        contains the title, return the book
        :param title: title of a book
        :return: the book that matches title from parameter
        """

        for element in self.book_list:
            if element.title == title:
                return element

        print("Book could not be found")

    def add_book(self, book):
        """
        Adds a book to the library's collection if the collection
        doesn't already contain the book
        """
        if book not in self.book_list:
            self.book_list.append(book)

    def remove_book(self, call_number):
        """
        Removes a book from the library's book collection
        :param call_number: A book's call number
        :return: Message telling user whether book was successfully
        deleted
        """
        for element in self.book_list:
            if element.call_number == call_number:
                self.book_list.remove(element)
                return "book successfully removed"
        return "book could not be found"

    def check_out(self, call_number):
        """
        Checks a book out from the library if it exists.
        Everytime a book is checked out, the number of copies available
        of the book is decremented by 1.
        :param call_number: A book's call number
        :return: Message telling user whether the check out was
        successful
        """
        for element in self.book_list:
            if element.call_number == call_number:
                element.num_copies -= 1
                return "book successfully checked-out"
        return "book could not be found"

    def return_book(self, call_number):
        """
        Returns a book to the library's collection if the book exists
        in the collection. Once a book is returned, its number of copies
         available is incremented by 1
        :param call_number: a book's call number
        :return: Message telling user whether the return was successful
        """
        for element in self.book_list:
            if element.call_number == call_number:
                element.num_copies += 1
                return "book successfully returned"
        return "book could not be found"

    def display_available_books(self):
        """
        Prints out the list of available books and their details
        """
        for element in self.book_list:
            print(element)

def main():
    vpl = Library()
    vpl.add_book(Book('Shame', 'A0101', 'Salman Rushdie', 5))
    vpl.add_book(Book('The Double', 'A0102', 'Dostoevesky', 1))
    vpl.add_book(Book('AI Superpowers', 'B0101', 'Kai-Fu Lee', 2))

    while 1:
        prompt = '\nSelect an option:\n' \
            '1. Remove book by call number \n' \
            '2. Check out book by call number\n' \
            '3. Return book by call number\n'\
            '4. Search for book by title\n'\
            '5. Display library catalogue\n'\
            '6. To exit\n'

        usr_input = input(prompt)

        while usr_input not in ['1', '2', '3', '4', '5', '6']:
            usr_input = input("Invalid input. Try again.\n" + prompt)

        def option_one():
            next_input = input('Input book\'s call number\n')
            print(vpl.remove_book(next_input))

        def option_two():
            next_input = input('Input book\'s call number\n')
            print(vpl.check_out(next_input))

        def option_three():
            next_input = input('Input book\'s call number\n')
            print(vpl.return_book(next_input))

        def option_four():
            next_input = input('Input book\'s title\n')
            print(vpl.find_books(next_input))

        method_dict = {1: option_one, 2: option_two, 3: option_three,
                       4: option_four,
                       5: vpl.display_available_books, 6: exit}

        method_dict[int(usr_input)]()

if __name__ == '__main__':
    main()




