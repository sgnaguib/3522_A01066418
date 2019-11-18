from pathlib import Path
import pandas as pd



class Order:
    """
    Stores the order details adn the associated factory
    """
    def __init__(self, factory, order_details):
        self.factory = factory
        self.order_number = order_details


class OrderProcessor:
    """
    Uses the pandas library to extratct the open
    and orders spreadsheet and extract its orders one at a time

    """
    def __init__(self):
        self.df = None
        self.order_iter = None

    def open_order_sheet(self, path):
        file = Path(path)
        self.df = pd.read_excel(file)
        self.order_iter = self.df.iterrows()
        # for order in self.order_iter:
        #     print(order)

        # print(orders_iter.__next__())

    def process_next_order(self):

        next_order = next(self.order_iter)

        order_details = next_order[1]

        print(order_details['Brand'])

        return_order = Order()

        return order_details
        # print(self.next_order())


class GarmentMaker:

    def __init__(self):
        self.shirts_men = []
        self.shirts_women = []
        self.socks_unisex = []

        self.processor = OrderProcessor()

    def open_order_sheet(self, path):
        self.processor.open_order_sheet(path)

    def process_orders(self):
        orders_left = True
        while orders_left:
            try:
                print(self.processor.process_next_order())
            except StopIteration:
                orders_left = False


def main():
    # path = input("Please input the directory of "
    #                  "the Excel Order Sheet\n")

    path = Path.cwd()/'orders.xlsx'

    g_maker = GarmentMaker()

    g_maker.open_order_sheet(path)

    g_maker.process_orders()


if __name__ == '__main__':
    main()
