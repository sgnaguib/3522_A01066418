from datetime import datetime


class TimeKeeper:
    """Lets the game class know how much time has elapsed between
    tamagotchi status checks"""

    last_check = None
    current_check = None

    @classmethod
    def time_check(cls):
        cls.current_check = datetime.now()
        temp = cls.last_check
        cls.last_check = cls.current_check
        if temp is None:
            return 0
        else:
            return (cls.current_check - temp).seconds

