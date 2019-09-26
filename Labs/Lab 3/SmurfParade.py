class SmurfParade:
    """
    Maintains a sequence of elements.
    This calls counts the number of elements it has
    It retrieves an element using square bracket notation
    It retieves an element by value
    Can check whether an element is inside the SmurfParade using
    the in and no in operators
    Produces an iteraotr that an be used with iter() and for-loops
    """

    def __init__(self):
        self.smurf_list = []

    def append(self, item):
        self.smurf_list.append(item)

    def __len__(self):
        return len(self.smurf_list)

    def __contains__(self, item):
        return item in self.smurf_list

    def __iter__(self):
        return iter(self.smurf_list)

    def __getitem__(self, key):
        return self.smurf_list[key]

    def count(self, item):
        return self.smurf_list.count(item)

    def index(self, item):
        return self.smurf_list.index(item)

    def __reversed__(self):
        return reversed(self.smurf_list)

def main():
    parade = SmurfParade()
    parade.append("a")
    parade.append("a")
    parade.append("b")
    parade.append("e")
    print(parade.count("a"))
    print(parade[2])
    print(parade.index("e"))
    print("b" in parade)
    print("c" in parade)


    for smurf in parade:
        print(smurf)

    # reversed_parade = reversed(parade)
    #
    # for smurf in reversed_parade:
    #     print(smurf)


if __name__ == "__main__":
    main()


