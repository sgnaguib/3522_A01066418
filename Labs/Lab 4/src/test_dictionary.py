from unittest import TestCase
from dictionary import Dictionary
from pathlib import Path


class TestDictionary(TestCase):

    def setUp(self):
        self.dictionary = Dictionary()

    def test_load_dictionary_valid_file(self):
        """
        Standard case, loading a valid json file
        """
        self.dictionary.load_dictionary('data.json')
        self.assertEqual(self.dictionary.loaded, True)

    def test_load_dictionary_invalid_file(self):
        """
        Trying to load a .txt file to the dictionary
        """
        self.assertRaises(Exception, self.dictionary.load_dictionary,
                          'data.txt')

    def test_query_definition_valid(self):
        """
        Query word that the dictionary contains
        """
        self.dictionary.load_dictionary(Path.cwd()/'data.json')
        given = ['A distinct unit of language '
                 '(sounds in speech or written letters) with a '
                 'particular meaning, composed of one or more morphemes,'
                 ' and also of one or more phonemes that determine '
                 'its sound pattern.']
        self.assertEqual(self.dictionary.query_definition('word'),
                         given)

    def test_query_definition_missing(self):
        """
        Query word that isn't contained in the dictionary
        """
        self.dictionary.load_dictionary(Path.cwd() / 'data.json')
        self.assertRaises(Exception, self.dictionary.
                          query_definition,
                         'blah blah')