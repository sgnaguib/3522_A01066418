class Book:
    """
    Represents a library book that can be check out.
    """

    def __init__(self, title, call_number, author, num_copies):
        self.title = title
        self.call_number = call_number
        self.author = author
        self.num_copies = num_copies

    def check_availability(self):
        """
        Checks whether there are still copies of the book available
        :return: whether there is at least 1 copy of the book available
        """
        return self.num_copies > 0

    def __str__(self):
        """
        Provides a string displaying the book's details
        :return: formatted string of book's details
        """
        return (
                f"Title: {self.title}, Call #: {self.call_number},"
                f" Author: {self.author}, Copies available: {self.num_copies}"
                )

