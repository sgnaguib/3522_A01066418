from random import randrange
from random import randint
from datetime import datetime


class Asteroid():

    id_count = 0

    def __init__(self, radius, position, velocity, timestamp):
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.time_created = timestamp
        self.id = Asteroid.id_count
        Asteroid.id_count += 1

    def set_radius(self, value):
        self.radius = value

    def get_radius(self):
        return self.radius

    def set_position(self, value):
        self.position = value

    def get_position(self, value):
        return self.position

    def set_velocity(self, value):
        self.velocity = value

    def get_velocity(self):
        return self.velocity

    def set_timestamp(self, value):
        self.timestamp = value

    def get_timestamp(self):
        return self.timestamp

    def move(self):
        # Modifies asteroid position using velocity
        # Returns the new position as a tuple of x,y, and z coordinates
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]
        return tuple(self.position)

    @classmethod
    def rand_asteroid(cls, max_velocity, max_position, max_radius):
        # Creates an asteroid with a random radius between [1,4], within a random position in a
        # cube 100 meters per side, with a velocity no greater than 5 m/s in any direction
        rand_vx = randint(-max_velocity, max_velocity)
        rand_vy = randint(-max_velocity, max_velocity)
        rand_vz = randint(-max_velocity, max_velocity)
        velocity = [rand_vx, rand_vy, rand_vz]
        random_position = [randrange(max_position), randrange(max_position), randrange(max_position)]
        random_radius = randrange(max_radius)+1
        return Asteroid(random_radius, random_position, velocity, datetime.now())

    def __str__(self):
        return f"Asteroid id: {self.id}, position: {self.position},"\
                f"velocity: {self.velocity}, time created: {self.time_created}"


