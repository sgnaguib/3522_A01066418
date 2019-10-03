from enum import Enum


class FileExtensions(Enum):
    TXT = 1
    JSON = 2

class InvalidFileTypeError:
    def __init__(self, invalid_char):
        super().__init__(f"Error: the type of file you have tried "
                         f"to load is invalid")
        self.invalid_char = invalid_char

class FileHandler:

    @staticmethod
    def load_data(self, path, file_extension):
        """
        Responsbile for checking the file extension and
        reading the file accordingly. Raises exceptions if...
        :param path:
        :param file_extension:
        :return:
        """

    def write_lines(self, path, lines):
        """
        Appends the given lines to a text file
        :param path:
        :param lines:
        :return:
        """

