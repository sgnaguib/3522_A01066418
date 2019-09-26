from activity import Activity


class ActivityList:
    """
    List of activites used in the tamagotchi game.
    """

    def __init__(self):
        p_fight = Activity('pillow fight', 20)
        s_contest = Activity('staring contest', 30)
        monopoly = Activity('monopoly', 15)
        self.act_list = [p_fight, s_contest, monopoly]

    def get_act_list(self):
        return self.act_list
