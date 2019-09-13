from asteroid import Asteroid
import datetime
import time

class Controller:
    """
    Controls the creation and movement of Asteroid objects.
    """

    def __init__(self):
        """
        Creates a hundred asteroid objects and stores them in a list.
        """
        self.asteroid_list = []
        for index in range(0, 100):
            self.asteroid_list.append(Asteroid.rand_asteroid(5,100,4))

    def simulate(self, seconds):
        """
        Starting at the beginning of a new second on the computer's clock, this method
        moves all asteroids once a second for the number of seconds specified by the parameter
        :param seconds: the number of times the asteroids will be moved
        """

        seconds_count = 0
        comp_time = datetime.datetime.now().microsecond
        wait_time = 1 - comp_time/1e6
        time.sleep(wait_time)
        while seconds_count < seconds:
            time.sleep(1)
            print(f"\nAfter {seconds_count+1} seconds")
            for element in self.asteroid_list:
                element.move()
                print(element)
            seconds_count += 1



def main():
    """
    Initiates a controller object and drives the program
    """
    test_controller = Controller()
    for element in test_controller.asteroid_list:
        print(element)
    test_controller.simulate(5)


if __name__ == "__main__":
    main()





