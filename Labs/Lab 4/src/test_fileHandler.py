from unittest import TestCase
from file_handler import FileHandler
from file_handler import FileExtensions
from file_handler import InvalidFileTypeError
from pathlib import Path



class TestFileHandler(TestCase):
    """
    Unit tests for FileHandler class
    """

    def test_load_data_wrong_file_type(self):
        """
        Testing case where user pases JSON enum but the path is not
        to a .json file - this should raise a type error
        """
        self.assertRaises(InvalidFileTypeError,
                          FileHandler.load_data, Path.cwd()/'test.txt',
                          FileExtensions.JSON)

    def test_load_data_nonexistant_file(self):
        """Testing case where file does not exist - should raise
        an error"""
        self.assertRaises(Exception, FileHandler.load_data, Path.cwd() /
                          'blah.txt', FileExtensions.TXT)

    def test_write_lines(self):


        with open(Path.cwd() / 'test.txt', mode='r', encoding='utf-8') \
                as text_file:
            before = text_file.read()
        FileHandler.write_lines(Path.cwd() / 'test.txt',
                                'it worked!')
        with open(Path.cwd() / 'test.txt', mode='r', encoding='utf-8') \
                as text_file:
            after = text_file.read()
        self.assertEqual(before + 'it worked!', after)
