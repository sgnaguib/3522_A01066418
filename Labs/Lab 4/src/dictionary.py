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
        self.loaded = False

    def load_dictionary(self, filepath):
        """Responsible for loading
        data into the dictionary
        """
        self.entries = FileHandler.load_data(filepath,
                                             FileExtensions.JSON)
        if self.entries:
            # if dictionary is not empty.
            self.loaded = True


    def query_definition(self, word):
        """
        Returns the definition of a given word
        :param word:
        :return:
        """
        return self.entries[word]


def main():
    # FileHandler.load_data(Path.cwd()/'data.json', FileExtensions.JSON)
    # FileHandler.write_lines(Path.cwd()/'check.txt', "Does this work?\n"
    #                                                 "really?")
    dictionary = Dictionary()
    dictionary.load_dictionary(Path.cwd()/'data.json')
    #print(dictionary.query_definition("bay"))

    while True:
        usr_input = input("Please enter a word you would like to query "
                          "in the dictionary\nor enter 'exitprogram' "
                          "to quit\n")
        if usr_input == 'exitprogram':
            print("Okay, goodbye!")
            exit()
        else:
            print(f"{dictionary.query_definition(usr_input)}\n")



if __name__ == '__main__':
    main()
