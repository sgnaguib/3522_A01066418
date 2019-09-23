import activity


class StaringContest(activity.Activity):
    """
    Represents a staring contest, a kind of activity for a tamogatchi
    """

    def __init__(self):
        super().__init__('staring contest')

    def play(self, tamagotchi):
        happiness_dict = {'Mussolini': 10, 'Napoleon': 15,
                          'Stalin': 20}
        return happiness_dict[tamagotchi.name]


