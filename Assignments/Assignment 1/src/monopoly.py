import activity


class Monopoly(activity.Activity):
    """
    Represents monopoly, a kind of activity for a tamogatchi
    """

    def __init__(self):
        super().__init__('monopoly')

    def play(self, tamagotchi):
        happiness_dict = {'Mussolini': 15, 'Napoleon': 10,
                          'Stalin': 10}
        return happiness_dict[tamagotchi.name]


