import abc


class Item(abc.ABC):
    """
    Represents a library item
    """

    def __init__(self, title, call_number, num_copies):
        self.title = title
        self.call_number = call_number
        self.num_copies = num_copies

    def check_availability(self):
        """
        Checks whether there are still copies of the book available
        :return: whether there is at least 1 copy of the book available
        """
        return self.num_copies > 0

    @abc.abstractmethod
    def __str__(self):
        pass
