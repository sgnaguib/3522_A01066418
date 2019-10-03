from file_handler import FileHandler
from file_handler import FileExtensions
from pathlib import Path
import json
"""
Modules is responsible for housing the dictionary class and
the driver methods
"""



class Dictionary:
    """

    """

    def __init__(self):
        self.entries = {}
    def load_dictionary(self, filepath):
        """Responsible for loading
        data into the dictionary
        """
        self.entries = FileHandler.load_data(filepath,
                                             FileExtensions.JSON)
        print(self.entries["acidity"])

    def query_definition(self, word):
        """
        Returns the definition of a given word
        :param word:
        :return:
        """


def main():
    # FileHandler.load_data(Path.cwd()/'data.json', FileExtensions.JSON)
    # FileHandler.write_lines(Path.cwd()/'check.txt', "Does this work?\n"
    #                                                 "really?")
    dictionary = Dictionary()
    dictionary.load_dictionary(Path.cwd()/'data.json')


if __name__ == '__main__':
    main()
