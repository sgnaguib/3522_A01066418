from file_handler import FileHandler
from file_handler import FileExtensions
from pathlib import Path
"""
Modules is responsible for housing the dictionary class and
the driver methods
"""


class Dictionary:
    """
    Represents a dictionary that gets loaded from a JSON file.
    Once the dictionary is loaded, words can be queried. The word query
    is case insensitive. The dictionary keeps track of all the words
    queried and can print a list of them to a .txt file.
    """

    def __init__(self):
        self.entries = {}
        self.queried_words = {}
        self.loaded = False

    def load_dictionary(self, filepath):
        """Responsible for loading
        data into the dictionary
        """
        try:
            self.entries = FileHandler.load_data(filepath,
                                                FileExtensions.JSON)
        except Exception as e:
            raise Exception("Could not load file")
        if self.entries:
            # if dictionary is not empty.
            self.loaded = True

    def query_definition(self, word):
        """
        Returns the definition of a given word
        :param word:
        :return:
        """
        try:
            self.queried_words[word] = self.entries[word]
            return self.entries[word]
        except:
            try:
                self.queried_words[word.title()] = self.entries[word.title()]
                return self.entries[word.title()]
            except:
                try:
                    self.queried_words[word.upper()] = self.entries[word.upper()]
                    return self.entries[word.upper()]
                except:
                    try:
                        self.queried_words[word.lower()] = self.entries[
                            word.lower()]
                        return self.entries[word.lower()]
                    except:
                        raise Exception(
                            "The word does not exist in the "
                            "dictionary.\n")

    def formatted_query_list(self):
        """
        formats the dictionary of queried words and their definition
        as a string with. The string format is word \n definition \n
        word \n definition, etc
        """
        formatted_list = ""
        for element in self.queried_words:
            formatted_list += (f"{element}\n"
                               f"{self.queried_words[element]}\n")
        return formatted_list

    def write_query_list(self, path):
        """
        Writes the list of queried words and their definitions to
        a .txt file
        """
        FileHandler.write_lines(Path.cwd() / path,
                                self.formatted_query_list())


def main():
    dictionary = Dictionary()
    dictionary.load_dictionary(Path.cwd()/'data.json')

    while True:
        usr_input = input("Please enter a word you would like to query "
                          "in the dictionary\nor enter 'exitprogram' "
                          "to quit\n")
        if usr_input.lower() == 'exitprogram':
            print("Okay. goodbye!")
            dictionary.write_query_list('queried_words.txt')

            exit()
        else:
            try:
                print(f"{dictionary.query_definition(usr_input)}\n")
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
