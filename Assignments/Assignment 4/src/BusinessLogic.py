from pathlib import Path
import pandas as pd
from GarmentFactory import *

"""
This module is responsible for getting order information from 
an excel spreadsheet, creating garments specified by the orders
and printing a report.
"""


class Order:
    """
    Stores the order details adn the associated factory
    """
    def __init__(self, order_details):
        self.details = order_details
        self.garment_type = self.details['Garment']
        self.count = self.details['Count']
        self.brand = self.details['Brand']
        self.kw_details = {'style': self.details['Style name'],
                           'size': self.details['Size'],
                           'colour': self.details['Colour'],
                           'textile': self.details['Textile'],
                           'sport': self.details['Sport'],
                           'number_pockets': self.details
                           ['Hidden Zipper Pockets'],
                           'indoor_outdoor_type': self.details
                           ['Indoor/Outdoor'],
                           'requires_iron': self.details
                           ['Requires Ironing'],
                           'number_buttons': self.details['Buttons'],
                           'contains_silver': self.details['Silver'],
                           'contrast_colour': self.details['Stripe'],
                           'requires_dry_cleaning': self.details
                           ['Dry Cleaning'],
                           'is_articulated': self.details['Articulated'],
                           'length': self.details['Length'],
                           'garment_type': self.details['Garment']
                           }


class OrderProcessor:
    """
    Uses the pandas library to extract the open
    and orders spreadsheet and extract its orders one at a time

    """

    def __init__(self):
        self.data_frame = None
        self.order_iter = None

    def open_order_sheet(self, path) -> bool:
        """opens an excel file"""
        file = Path(path)
        valid = True
        try:
            self.data_frame = pd.read_excel(file)
        except FileNotFoundError:
            print("File Could Not Be Found.")
            valid = False
        else:
            self.order_iter = self.data_frame.iterrows()
        finally:
            return valid

    def process_next_order(self):
        """Gets the next row from the excel sheet,
        and creates an order based on the extracted
        information."""
        next_order = next(self.order_iter)
        order_details = next_order[1]
        details_dict = order_details.to_dict()
        order = Order(details_dict)

        return order


class GarmentMaker:
    """
    Responsible for getting the orders from the
    OrderProcessors and passing the order details to the appropriate
    BrandFactory
    """

    def __init__(self):
        self.shirts_men = []
        self.shirts_women = []
        self.socks_unisex = []
        self.report = []
        self.processor = OrderProcessor()

    def open_order_sheet(self, path):
        return self.processor.open_order_sheet(path)

    def process_orders(self):
        """Gets orders from the processor and creates
        the garments according to the order specifications,
        then add the orders to the daily report"""
        orders_left = True
        while orders_left:
            try:
                order = self.processor.process_next_order()
            except StopIteration:
                orders_left = False
            else:
                garments = self.create_garments(order)
                self.add_garments(garments, order.garment_type)
                self.add_to_report(order.brand, order.garment_type,
                                   garments)

    def create_garments(self, order):
        """Takes in an order and creates the type and quantity of the
        garment specified by the order."""

        factory_dict = {'Lululime': LuluLimeFactory(),
                        'PineappleRepublic': PineappleRepublicFactory(),
                        'Nika': NikaFactory()}

        factory = factory_dict[order.details['Brand']]

        product_dict = {'ShirtMen': factory.create_shirt_men,
                        'ShirtWomen': factory.create_shirt_women,
                        'SockPairUnisex': factory.create_socks_unisex}

        garments = []
        for i in range(0, order.count):
            garment = \
                product_dict[order.garment_type](**order.kw_details)
            garments.append(garment)

        return garments

    def add_garments(self, garments, garment_type):
        """Adds a list of garments to one of the
        GarmentMaker's lists, shirts_men, shirts_women or
        socks_unisex"""

        garment_dict = {'ShirtMen': self.shirts_men,
                        'ShirtWomen': self.shirts_women,
                        'SockPairUnisex':
                            self.socks_unisex}

        garment_dict[garment_type].extend(garments)

    def add_to_report(self, brand, garment_type, garments):
        report_row = (brand, garment_type, garments)
        self.report.append(report_row)

    def print_report(self):
        print("The Report of Today's Filled Orders:\n")
        for row in self.report:
            print(f"{row[0]}, {row[1]}")
            for element in row[2]:
                print(element)
            print("-"*80)


def main():
    prompt = "Please the path of the Excel Order Sheet\n"
    invalid_file = True
    while invalid_file:

        file_path = input(prompt)
        if file_path == 'exit':
            break

        g_maker = GarmentMaker()

        if g_maker.open_order_sheet(file_path):
            g_maker.process_orders()
            g_maker.print_report()
            invalid_file = False
        else:
            prompt = "Please try another file name or type 'exit' to " \
                     "quit the program\n"
            invalid_file = True


if __name__ == '__main__':
    main()
