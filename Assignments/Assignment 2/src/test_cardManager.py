from unittest import TestCase
from cardmanager import CardManager
import os
from pathlib import Path


class TestCardManager(TestCase):

    def setUp(self):
        self.manager = CardManager()
        self.test_inputs = {"card_name": "Tim Horton's Card",
                            "business_name": "Tim Horton's",
                            "card_number": "123",
                            "expiry_date": "10/22"}
        self.new_card = \
            self.manager.add_card('Gift Card', **self.test_inputs)

    def test_add_card(self):
        """Tests case where a valid card type is added"""
        self.assertEqual(self.manager.search_card("Tim Horton's Card").
                         __dict__
                         , self.test_inputs)

    def test_add_invalid_card_type(self):
        self.assertRaises(Exception, self.manager.add_card, 'Random Card',
                          **self.test_inputs)

    def test_search_card(self):
        self.assertEqual(self.manager.search_card("Tim Horton's Card"),
                         self.new_card)

    def test_delete_card(self):
        """Tests case where an existent card is deleted"""
        self.assertTrue(self.manager.delete_card("Tim Horton's Card"))

    def test_delete_non_existent_card(self):
        self.assertEqual(self.manager.delete_card("Random Card"), False)

    def test_export_cards(self):
        file_name = self.manager.export_cards()
        self.assertTrue(os.path.exists(Path.cwd()/file_name))
