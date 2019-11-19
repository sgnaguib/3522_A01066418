from pathlib import Path
import pandas as pd
from GarmentFactory import *


class Order:
    """
    Stores the order details adn the associated factory
    """
    def __init__(self, factory, order_details):
        self.factory = factory
        self.details = order_details
        self.garment_type = self.details['Garment']
        self.count = self.details['Count']
        self.brand = self.details['Brand']
        self.kw_details = {'style': self.details['Style name'],
                           'size': self.details['Size'],
                           'colour': self.details['Colour'],
                           'textile': self.details['Textile'],
                           'sport': self.details['Sport'],
                           'number_pockets': self.details['Hidden Zipper Pockets'],
                           'indoor_outdoor_type': self.details['Indoor/Outdoor'],
                           'requires_iron': self.details['Requires Ironing'],
                           'number_buttons': self.details['Buttons'],
                           'contains_silver': self.details['Silver'],
                           'contrast_colour': self.details['Stripe'],
                           'requires_dry_cleaning': self.details['Dry Cleaning'],
                           'is_articulated': self.details['Articulated'],
                           'length': self.details['Length'],
                           'garment_type': self.details['Garment']

    }


class OrderProcessor:
    """
    Uses the pandas library to extratct the open
    and orders spreadsheet and extract its orders one at a time

    """
    factory_dict = {'Lululime': LuluLimeFactory(),
                    'PineappleRepublic': PineappleRepublicFactory(),
                    'Nika': NikaFactory()}

    def __init__(self):
        self.df = None
        self.order_iter = None

    def open_order_sheet(self, path):
        file = Path(path)
        try:
            self.df = pd.read_excel(file)
        except FileNotFoundError:
            print("No such file exists in this directory")
            return False
        else:
            self.order_iter = self.df.iterrows()
            return True

    def process_next_order(self):
        next_order = next(self.order_iter)
        order_details = next_order[1]

        brand_factory = self.factory_dict[order_details['Brand']]

        details_dict = order_details.to_dict()

        order = Order(brand_factory, details_dict)

        return order


class GarmentMaker:

    def __init__(self):
        self.shirts_men = []
        self.shirts_women = []
        self.socks_unisex = []

        self.report = []

        self.processor = OrderProcessor()

    def open_order_sheet(self, path):
        self.processor.open_order_sheet(path)

    def process_orders(self):
        orders_left = True
        while orders_left:
            try:
                order = self.processor.process_next_order()
            except StopIteration:
                orders_left = False
            else:
                garments = self.create_garments(order, order.count)
                self.add_garments(garments, order.garment_type)
                self.add_to_report(order.brand, order.garment_type,
                                   garments)

    def create_garments(self, order, count):

        factory = order.factory

        product_dict = {'ShirtMen': factory.create_shirt_men,
                        'ShirtWomen': factory.create_shirt_women,
                        'SockPairUnisex': factory.create_socks_unisex}

        garments = []
        for i in range(0, count):
            garment = product_dict[order.garment_type](**order.kw_details)
            garments.append(garment)

        return garments

    def add_garments(self, garments, garment_type):

        garment_dict = {'ShirtMen': self.shirts_men,
                        'ShirtWomen': self.shirts_women,
                        'SockPairUnisex':
                            self.socks_unisex}

        garment_dict[garment_type].extend(garments)

    def add_to_report(self, brand, garment_type, garments):
        """Report: Brand, garment_type, garment list"""

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
    prompt = "Please input the name of the Excel Order Sheet, " \
             "including the file extension\n" \
             "Note: the file should be in the same directory as this " \
             "program.\n"
    while True:

        file_name = input(prompt)
        if file_name == 'exit':
            break

        path = Path.cwd()/file_name

        g_maker = GarmentMaker()

        if g_maker.open_order_sheet(path):
            g_maker.process_orders()
            g_maker.print_report()
            break
        else:
            prompt = "Please try another file name or type 'exit' to " \
                     "quit the program\n"



if __name__ == '__main__':
    main()
