import argparse
from pathlib import Path
from asyncio_requests import *

"""This module contains the classes that handle user input and prints 
the users search result either to a .txt file or to the console."""


class InputHandler:
    """
    This class parses the arguments passed by the user through
    the command line.
    """

    def __init__(self):
        self.mode = None
        self.input = None
        self.expanded = None
        self.output = None

    def setup_request_commandline(self):
        """
        Comments written by Rahul:
        Implements the argparse module to accept arguments via the
        command line. This function specifies what these arguments are
        and parses it into an object of type InputHandler.
        If something goes wrong with provided arguments then the
        function prints an error message and exits the application.
        :return: The object of type RequestHandler with all the arguments
        provided in it.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("mode", choices=['pokemon', 'ability',
                                             'move'],
                            help="The application has to be opened "
                                 "in one of 3 specific modes, Pokemon,"
                                 "Ability or Move.")
        parser.add_argument("input",
                            help="Must take in a .txt file or a "
                                 "name/id.")

        parser.add_argument("--expanded", action='store_true',
                            help="When this flag is provided, certain "
                                 "pokedex attributes are expanded.")
        parser.add_argument("--output",
                            help="The text file that needs to be"
                                 "encrypted or decrypted")

        try:
            args = parser.parse_args()
            self.mode = args.mode
            self.input = args.input
            self.expanded = args.expanded
            self.output = args.output
        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()


class Pokedex:
    """
    Passes the input from the InputHandler to the requestHandler
    and processes the response by printing the returned poke objects
    either to the console or to a .txt file.
    """

    def __init__(self):
        self.input_handler = InputHandler()
        self.input_handler.setup_request_commandline()

        self.mode = self.input_handler.mode
        self.input = self.input_handler.input
        self.expanded = self.input_handler.expanded
        self.output = self.input_handler.output

        self.request_handler = RequestHandler(self.mode)

    def get_output(self):
        """
        Prints the response result to the console or to a .txt file.
        """
        output_data = str(self.process_input())

        if self.output is None:
            print(output_data)
            # output_data
        elif self.output.endswith('.txt'):
            with open(self.output, 'w') as file:
                file.write(output_data)
        else:
            print("Invalid file type for output. Only .txt file are "
                  "accepted as output files.\n")

    def process_input(self):
        """
        Determines whether to process the input as a single request
        or as a list of requests.
        :return: formatted response containing poke object(s)
        """
        if self.input.endswith('.txt'):
            try:
                input_list = self.get_file_inputs()
            except FileNotFoundError:
                return f"File {self.input} could not be found in " \
                       f"local directory"
            except Exception:
                return f"Error opening file"
            else:
                poke_objects = self.multiple_inputs(input_list)
                return self.format_multiple(poke_objects)
        else:
            return self.single_input()

    def get_file_inputs(self):
        """
        Splits a .txt into a list of the words it contains (delimited
        by whitespace).
        :return:
        """
        file_path = Path.cwd()/self.input

        with open(file_path, 'r') as file:
            text = file.read()

        lower_text = text.lower()
        input_list = lower_text.split()
        return input_list

    def multiple_inputs(self, input_list):
        """
        Takes in a list of poke object names or IDs and
        calls an asynchronous function to call a Poke API
        for information regarding the poke_objects.
        It returns the request results.
        :param input_list: a list of strings
        :return: a list of poke_objects
        """
        try:
            poke_objects = asyncio.run(
                self.request_handler.
                process_multiple_requests(input_list, self.expanded))
        except Exception:
            return "Error Processing Multiple Inputs."
        else:
            return poke_objects

    def format_multiple(self, poke_objects):
        """
        Takes a list of poke_objects and formats them so that
        they each objects is clearly demarcated.
        :param poke_objects:
        :return:
        """
        formatted = ""
        for poke in poke_objects:
            formatted += str(poke) + '\n'
            formatted += '-' * 80
            formatted += '\n'
        return formatted

    def single_input(self):
        """Takes in the name of id of a poke_object and
        calls a function to make a request to the PokeAPI
        for detailed information regarding that poke_object."""
        poke_object = asyncio.run(
            self.request_handler.process_single_request(self.input,
                                                        self.expanded))
        return poke_object


def main():
    pokedex = Pokedex()
    pokedex.get_output()


if __name__ == '__main__':
    main()
