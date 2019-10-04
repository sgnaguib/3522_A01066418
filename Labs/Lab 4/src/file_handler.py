from pathlib import Path
from enum import Enum
import json


class FileExtensions(Enum):
    """Enumerated type, with two valid states: TXT, JSON"""
    TXT = 1
    JSON = 2


class InvalidFileTypeError(Exception):
    def __init__(self):
        super().__init__(f"Error: the type of file you have tried "
                         f"to load is invalid")

class FileHandler:
    """
    has functions for loading data from a JSON or TXT file and
    writing lines to as a txt file
    """

    @staticmethod
    def load_data(path, file_extension):
        """
        Responsbile for checking the file extension and
        reading the file accordingly. Raises exceptions if...
        """
        file = Path(path)
        if file.is_file():
        # file exists
            if file_extension == FileExtensions.JSON:
                try:
                    with open(path, mode='r', encoding='utf-8') \
                            as json_file:
                        return json.load(json_file)
                except Exception:
                    raise InvalidFileTypeError()

            if file_extension == FileExtensions.TXT:
                with open(path, mode='r',
                                encoding='utf-8') as text_file:
                    return text_file.read()

        else:
            raise Exception("Error. The file does not exist.")

    @staticmethod
    def write_lines(path, lines):
        """
        Appends the given lines to a text file
        """
        with open(path, mode='a') as my_text_file:
            my_text_file.write(lines)


