from pathlib import Path
from enum import Enum


class FileExtensions(Enum):
    TXT = '.txt'
    JSON = '.json'

class InvalidFileTypeError:
    def __init__(self, invalid_char):
        super().__init__(f"Error: the type of file you have tried "
                         f"to load is invalid")
        self.invalid_char = invalid_char

class FileHandler:

    @staticmethod
    def load_data(path, file_extension):
        """
        Responsbile for checking the file extension and
        reading the file accordingly. Raises exceptions if...
        :param path:
        :param file_extension:
        :return:
        """
        test = '.txt'
        print(FileExtensions.TXT.value)
        file = Path(path)
        if file.is_file():
        # file exists, check that extensions match
            print('it exists')
            if test.lower().endswith((FileExtensions.JSON.value,
                                     FileExtensions.TXT.value)):
                print("extensions match")
        else:
            print("doesn't exist")

    @staticmethod
    def write_lines(self, path, lines):
        """
        Appends the given lines to a text file
        :param path:
        :param lines:
        :return:
        """

