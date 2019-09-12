import Asteroid
from random import randrange

class Controller:

    def __init__(self):
        asteroid_list = []
        for index in range(0, 100):
            asteroid_list.append(Asteroid.rand_asteroid)

    def simulate(self, seconds):
        for element in self.asteroid_list:
            self.asteroid_list[element].move()





