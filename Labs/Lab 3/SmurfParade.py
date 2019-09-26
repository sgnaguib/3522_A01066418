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

    # def __iter__(self):
    #     return iter(self.smurf_list)

    def __getitem__(self, key):
        return self.smurf_list[key]

    def count(self, item):
        return self.smurf_list.count(item)

    def index(self, item):
        return self.smurf_list.index(item)

    def __reversed__(self):
        return self.smurt_list.reverse()

def main():
    parade = SmurfParade()
    parade.append("hello")
    parade.append("hi")
    parade.append("")
    print(parade)
    for smurf in parade:
        print(smurf)


if __name__ == "__main__":
    main()



# list = []
# list.append("huh?")
# smurf_p = SmurfParade()
# print(len(smurf_p))
# smurf_p.append("Smurf1")
# smurf_p.append("Smurf2")
# print(len(smurf_p))

# my_list = [1,2,3,4]
# print(my_list)
# print(reversed(my_list))
# print(list(reversed(my_list)))

#my_iter = iter([1,2,3,4])
# print(type(my_iter))
# print(next(my_iter))