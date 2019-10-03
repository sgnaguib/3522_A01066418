from pathlib import Path
from enum import Enum
import json


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
    def load_data(path, file_extension):
        """
        Responsbile for checking the file extension and
        reading the file accordingly. Raises exceptions if...
        :param path:
        :param file_extension:
        :return:
        """
        file = Path(path)
        if file.is_file():
        # file exists, check that extensions match
            print('it exists')
            if file_extension == FileExtensions.JSON:
                print('its a json!')
                json_file = open(path, mode='r', encoding='utf-8')
                return json.load(json_file)
            if file_extension == FileExtensions.TXT:
                print("its a txt!")
                text_file = open(path, mode='r',
                                encoding='utf-8')
                return text_file.read()

        else:
            print("doesn't exist")

    @staticmethod
    def write_lines(path, lines):
        """
        Appends the given lines to a text file
        :param path:
        :param lines:
        :return:
        """
        with open(path, mode='a') as my_text_file:
            my_text_file.write(lines)

