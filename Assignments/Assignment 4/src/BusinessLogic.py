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
                           'length': self.details['Length']

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
        self.df = pd.read_excel(file)
        self.order_iter = self.df.iterrows()

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

        self.processor = OrderProcessor()

    def open_order_sheet(self, path):
        self.processor.open_order_sheet(path)

    def get_orders(self):
        orders_left = True
        while orders_left:
            try:
                order = self.processor.process_next_order()
                self.process_order(order)
            except StopIteration:
                orders_left = False

    def process_order(self, order):

        factory = order.factory
        product_details = order.details
        garment_type = product_details['Garment']

        product_dict = {'ShirtMen': factory.create_shirt_men,
                        'ShirtWomen': factory.create_shirt_women,
                        'SockPairUnisex': factory.create_socks_unisex}

        print(product_details)
        # product_dict[garment_type](**product_details)




def main():
    # path = input("Please input the directory of "
    #                  "the Excel Order Sheet\n")

    path = Path.cwd()/'orders.xlsx'

    g_maker = GarmentMaker()

    g_maker.open_order_sheet(path)

    g_maker.get_orders()


if __name__ == '__main__':
    main()
