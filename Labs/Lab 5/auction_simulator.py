import random
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
        self.starting_price = float(starting_price)
        self.auctioneer = Auctioneer(bidders)

    def place_first_bid(self):
        print(f"Auctioninng {self.item} starting at "
              f"${round(self.starting_price,1)}")
        self.auctioneer.place_bid(self.starting_price, None)

    def print_winner(self):
        print(f"The winner of the auction is "
              f"{self.auctioneer.highest_current_bidder} at "
              f"${round(self.auctioneer.highest_current_bid, 1)}")

    def print_top_bids(self):
        print("Highest bids Per Bidder")
        top_bids = self.auctioneer.bidder_dictionary()
        for bidder in self.bidders:
            print(f"Bidder: {bidder}, "
                  f"Highest Bid: ${round(top_bids[bidder],1)}")


class Auctioneer:
    """
    Core object being observed in observer pattern.
    Auctioneer is responsible for keeping a list of bidders
    and calling them as functions if and when a new bid is accepted.
    """

    def __init__(self, bidders):
        self.bidders = bidders
        self.highest_current_bid = 0.0
        self.highest_current_bidder = None

    def place_bid(self, amount, bidder):
        """
        Allows auctioneer to accept a new bid if
        this bid is greater than the current_highest_bid
        :return:
        """
        if int(amount) > self.highest_current_bid:
            if bidder is not None and self.highest_current_bidder is not None:
                print(f"{bidder} bid {round(amount,1)} in "
                    f"response to {self.highest_current_bidder}'s"
                    f" bid of ${round(self.highest_current_bid,1)}")
            elif bidder is not None:
                print(f"{bidder} bid {round(amount, 1)} in "
                      f"response to starting bid of"
                      f" ${round(self.highest_current_bid, 1)}")
            self.highest_current_bid = amount
            self.highest_current_bidder = bidder
            self.notify_bidders(bidder)

    def notify_bidders(self, latest_bidder):
        """
        Allows auctioneer to notify all bidders of a new bid,
        except the bidder that placed the latest bid.
        :return:
        """
        for bidder in self.bidders:
            if bidder is not latest_bidder:
                bidder(self)

    def bidder_dictionary(self):
        top_bids = {bidder: bidder.highest_bid for bidder
                    in self.bidders}
        return top_bids


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
        self.budget = float(budget)
        self.bid_probability = float(bid_probability)
        self.bid_increase_perc = float(bid_increase_perc)
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
        if self is not auctioneer.highest_current_bidder and \
                self.budget > auctioneer.highest_current_bid and \
                random.random() < self.bid_probability:
            bid = auctioneer.highest_current_bid * \
                                 self.bid_increase_perc
            if bid > self.highest_bid:
                self.highest_bid = bid
            auctioneer.place_bid(bid, self)

    def __str__(self):
        return self.name


def main():
    print("Let's have an auction!\n")
    item_name = input("Please input the name of the item you'd like "
                      "auctioned.\n")

    invalid = True
    while invalid:
        try:
            starting_price = float(input("Please input the starting "
                                         "price of the item.\n"))
            invalid = False
        except ValueError:
            print("Your input was invalid. Please enter a number.")

    invalid = True
    while invalid:
        try:
            number_bidders = int(input("Please input the number of "
                                       "bidders you want to have.\n"))
            if number_bidders <= 0:
                raise Exception
            else:
                invalid = False
        except Exception:
            print("Your input was invalid. "
                  "Please enter an integer greater than zero")

    bidder_list = []
    count = 0
    while count < number_bidders:
        name = input(f"Please input bidder {count}'s name\n")

        invalid_input = True
        while invalid_input:
            try:
                budget = float(input(f"Please input bidder {count}'s "
                                     f"budget\n"))
                if budget > 0:
                    invalid_input = False
                else:
                    raise Exception
            except Exception:
                print("Please enter a number greater than 0.")

        invalid = True
        while invalid:
            try:
                bid_probability = float(input(f"Please input bidder {count}'s "
                                        f"bid probability\n"))
                if 1 > bid_probability > 0:
                    invalid = False
                else:
                    raise Exception
            except:
                print("Please enter a decimal between 0.0 and 0.99")

        invalid_input = True
        while invalid_input:
            try:
                bid_increase_perc = float(input(f"Please input bidder {count}'s bid "
                                  f"increase percentage\n"))
                if bid_increase_perc > 1:
                    invalid_input = False
                else:
                    raise Exception
            except Exception:
                print("Please enter a decimal greater than 1")

        bidder_list.append(Bidder(name, budget, bid_probability,
                                  bid_increase_perc))
        count += 1

    my_auction = Auction(bidder_list, item_name, starting_price)
    my_auction.place_first_bid()
    my_auction.print_winner()
    my_auction.print_top_bids()


if __name__ == "__main__":
    main()

