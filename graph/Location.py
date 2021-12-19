import copy
import math

class Location:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def copyLoc(cls, location):
        cls.x = copy.deepcopy(location.x)
        cls.y = copy.deepcopy(location.y)
        cls.z = copy.deepcopy(location.z)

    @classmethod
    def distance(cls, location):
        d_x = pow((location.x - cls.x),2)
        d_y = pow((location.y - cls.y),2)
        d_z = pow((location.z - cls.z),2)
        return math.sqrt(d_x + d_y + d_z)

    def x(self):
        return self.x

    def y(self):
        return self.y

    def z(self):
        return self.z

