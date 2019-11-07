import item


class DVD(item.Item):
    """
    Represents a library's DVD
    """

    def __init__(self, release_date,
                 region_code, **kwargs):
        super().__init__(**kwargs)
        self.release_date = release_date
        self.region_code = region_code

    def __str__(self):
        """
        Provides a string displaying the book's details
        :return: formatted string of book's details
        """
        return (
                f"Title: {self.title}, Call #: {self.call_number}, "
                f"Release Date: {self.release_date}, "
                f"Region Code: {self.region_code}, "
                f"Copies available: "
                f"{self.num_copies}"
                )