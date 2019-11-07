import item

class Journal(item.Item):
    """
    Represents a library journal
    """

    def __init__(self, issue_num,
                 publisher, **kwargs):
        super().__init__(**kwargs)
        self.issue_num = issue_num
        self.publisher = publisher

    def __str__(self):
        """
        Provides a string displaying the book's details
        :return: formatted string of book's details
        """
        return (
                f"Title: {self.title}, Call #: {self.call_number}, "
                f"Issue #: {self.issue_num}, "
                f"Publisher: {self.publisher}, "
                f"Copies available: "
                f"{self.num_copies}"
                )