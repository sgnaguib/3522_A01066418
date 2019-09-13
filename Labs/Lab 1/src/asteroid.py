from random import randrange
from random import randint
from datetime import datetime


class Asteroid():
    """
    Defines an asteroid that can be moved.
    """

    id_count = 0

    def __init__(self, radius, position, velocity, timestamp):
        """
        Constructs Asteroid and gives it a unique ID.
        :param radius: radius of asteroid
        :param position: a list of x,y,z coordinates of asteroid
        :param velocity: a list of x,y,z velocity of asteroid
        :param timestamp: timestamp of when asteroid was created
        """
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self._time_created = timestamp
        self._id = Asteroid.id_count
        Asteroid.id_count += 1

    def set_radius(self, value):
        """
        :param value: new asteroid radius.
        """
        self.radius = value

    def get_radius(self):
        """
        :return: asteroid's radius.
        """
        return self.radius

    def set_position(self, value):
        """
        :param value: new asteroid position.
        """
        self.position = value

    def get_position(self):
        """
        :return: asteroid's current position.
        """
        return self.position

    def set_velocity(self, value):
        """
        :param value: asteroid's new velocity.
        """
        self.velocity = value

    def get_velocity(self):
        """
        :return: asteroid's current velocity.
        """
        return self.velocity

    def get_timestamp(self):
        """
        :return: time that asteroid was created.
        """
        return self._time_created

    def move(self):
        """
        Modifies asteroid position using velocity.
        :returns: the new position as a tuple of x,y, and z coordinates
        """
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]
        return tuple(self.position)

    @classmethod
    def rand_asteroid(cls, max_velocity, max_position, max_radius):
        """
        Creates an asteroid with a random radius, position, and velocity.
        :param max_velocity: maximum velocity of asteroid
        :param max_position: maximum position of asteroid
        :param max_radius: maximum radius of asteroid
        :return: newly created asteroid
        """
        rand_vx = randint(-max_velocity, max_velocity)
        rand_vy = randint(-max_velocity, max_velocity)
        rand_vz = randint(-max_velocity, max_velocity)
        velocity = [rand_vx, rand_vy, rand_vz]
        random_position = [randrange(max_position), randrange(max_position), randrange(max_position)]
        random_radius = randrange(max_radius)+1
        return Asteroid(random_radius, random_position, velocity, datetime.now())

    def __str__(self):
        """
        :return: Description of Asteroid's attributes
        """
        return f"Asteroid id: {self._id}, position: {self.position},"\
                f"velocity: {self.velocity}, time created: {self._time_created}"


