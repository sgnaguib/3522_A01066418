from pathlib import Path
from unittest import TestCase

from BusinessLogic import GarmentMaker


class TestGarmentMaker(TestCase):

    def setUp(self):
        self.g_maker = GarmentMaker()
        path = Path.cwd() / 'orders_small.xlsx'
        self.g_maker.open_order_sheet(path)
        self.first_order = self.g_maker.processor.process_next_order()

    def test_open_order_sheet(self):
        """valid path"""
        path = Path.cwd() / 'orders_small.xlsx'
        self.assertTrue(self.g_maker.open_order_sheet(path))

    def test_open_order_sheet_invalid(self):
        """invalid path"""
        path = Path.cwd() / 'so_much_work.xlsx'
        self.assertFalse(self.g_maker.open_order_sheet(path))

    def test_create_garments(self):
        """Checks whether the garments are created in the quantity
        and of the type specified by the order"""
        garments = self.g_maker.create_garments(self.first_order)
        right_number = len(garments) == self.first_order.count
        right_type = garments[0].garment_type == \
                     self.first_order.garment_type

        self.assertTrue(right_number and right_type)

    def test_add_garments(self):
        """Checks whether the garments passed to the add_garment
        function successfully get added to the appropriate
        GarmentMaker list (shirt_men, shirt_women or socks_unisex),
        note that the first order is for 3 mens shirt"""
        garments = self.g_maker.create_garments(self.first_order)
        original_length = len(self.g_maker.shirts_men)
        self.g_maker.add_garments(garments,
                                  self.first_order.garment_type)
        new_length = len(self.g_maker.shirts_men)

        self.assertTrue(new_length == original_length + 3)

