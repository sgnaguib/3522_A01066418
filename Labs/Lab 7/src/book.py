import item


class Book(item.Item):
    """
    Represents a library book that can be check out.
    """

    def __init__(self, author, **kwargs):
        super().__init__(**kwargs)
        self.author = author

    def __str__(self):
        """
        Provides a string displaying the book's details
        :return: formatted string of book's details
        """
        return (
                f"Title: {self.title}, Call #: {self.call_number},"
                f" Author: {self.author}, Copies available: {self.num_copies}"
                )

