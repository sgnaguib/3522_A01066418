import activity


class PillowFight(activity.Activity):
    """
    Represents a pillowfight, a kind of activity for a tamogatchi
    """

    def __init__(self):
        super().__init__('pillow fight')

    def play(self, tamagotchi):
        happiness_dict = {'Mussolini': 15, 'Napoleon': 20,
                          'Stalin': 10}
        return happiness_dict[tamagotchi.name]


