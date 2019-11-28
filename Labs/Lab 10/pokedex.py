import argparse


class InputHandler:

    @staticmethod
    def setup_request_commandline():
        """
        Implements the argparse module to accept arguments via the command
        line. This function specifies what these arguments are and parses it
        into an object of type Request. If something goes wrong with
        provided arguments then the function prints an error message and
        exits the application.
        :return: The object of type Request with all the arguments provided
        in it.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("mode",
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
            print(f"Mode: {args.mode}")
            print(f"Input: {args.input}")
            print(f"Exapnded: {args.expanded}")
            print(f"Output: {args.output}")
        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()


def main():
    InputHandler.setup_request_commandline()


if __name__ == '__main__':
    main()
