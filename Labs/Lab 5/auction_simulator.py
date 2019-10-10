"""
Contains  all the classes for lab5.
"""

class Auction:
    """
    Auction is responsible for registering the bidders
    to the auctioneer. Once that is done, the auction
    starts by placing the starting_price as the first bid.
    """
    def __init__(self, bidders, item, starting_price):
        self.bidders = bidders
        self.item = item
        self.starting_price = starting_price
        self.auctioneer = Auctioneer(bidders)

    def place_first_bid(self):
        self.auctioneer.process_bid(self.starting_price)

class Auctioneer:
    """
    Core object being observed in observer pattern.
    Auctioneer is responsible for keeping a list of bidders
    and calling them as functions if and when a new bid is accepted.
    """

    def __init__(self, bidders):
        self.bidders = bidders
        self.highest_current_bid = 0
        self.highest_current_bidder = None

    def process_bid(self, amount):
        """
        Allows auctioneer to accept a new bid if
        this bid is greater than the current_highest_bid
        :return:
        """
    def notify_bidders(self):
        """
        Allows auctioneer to notify all bidders of a new bid,
        except the bidder that placed the latest bid.
        :return:
        """



class Bidder:
    """
    Person who place a bid during an auction by observing
    auctioneer. Bidders are notified and given
    a chance to place a new bid every time
    the auctioneer accepts a bid. A bidder cannot respond to
    their own bid.
    """
    def __init__(self, name, budget, bid_probability,
                 bid_increase_perc):
        self.name = name
        self.budget = budget
        self.bid_probability = bid_probability
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __call__(self, auctioneer):
        """
        Allows the bidder to place a new bid with the auctioneer
        (This is only allowed if the bid is against another bidder,
        and the amount they bid is not greater than their
        budget. This method also accounts for their
        bid_probabiltiy
        :param auctioneer:
        :return:
        """


def main():
    print("Let's have an auction!\n")
    item_name = input("Please input the name of the item you'd like "
                      "auctioned.\n")
    starting_price = input("Please input the starting price of the item.\n")
    number_bidders = input("Please input the number of bidders you want to have.\n")
    bidder_list = []
    count = 0
    while count < int(number_bidders):
        name = input(f"Please input bidder {count}'s name\n")
        budget = input(f"Please input bidder {count}'s budget")
        bid_probability = input(f"Please input bidder {count}'s bid probability\n")
        bid_increase_perc = input(f"Please input bidder {count}'s bid"
                                  f"increase percentage")
        bidder_list.append(Bidder(name, budget, bid_probability,
                                  bid_increase_perc))
        count += 1

    my_auction = Auction(bidder_list, item_name, starting_price)


if __name__ == "__main__":
    main()

