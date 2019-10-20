from unittest import TestCase
from cardmanager import CardManager
from ui import UI



class TestUI(TestCase):


    def setUp(self):
        self.manager = CardManager()
        self.ui = UI(self.manager)

    def test_delete_card(self):
        self.ui

