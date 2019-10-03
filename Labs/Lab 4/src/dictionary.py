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
        self.queried_words = {}
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
        lower_word = word.lower()
        self.queried_words[lower_word] = self.entries[lower_word]
        return self.entries[lower_word]

    def formatted_query_list(self):
        formatted_list = ""
        for element in self.queried_words:
            formatted_list += (f"{element}\n"
                                f"{self.queried_words[element]}\n")
        return formatted_list


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

            FileHandler.write_lines(Path.cwd()/'queried_words.txt',
                                    dictionary.formatted_query_list())

            exit()
        else:
            print(f"{dictionary.query_definition(usr_input)}\n")



if __name__ == '__main__':
    main()
