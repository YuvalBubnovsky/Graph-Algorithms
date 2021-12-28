import copy
import math

'''
A class which represents a location in a 3D plane
'''


class Location:

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def copy_loc(cls, location):
        cls.x = copy.deepcopy(location.x)
        cls.y = copy.deepcopy(location.y)
        cls.z = copy.deepcopy(location.z)

    @staticmethod
    def distance(location1, location2):
        d_x = pow((location1.get_x() - location2.get_x()), 2)
        d_y = pow((location1.get_y() - location2.get_y()), 2)
        d_z = pow((location1.get_z() - location2.get_z()), 2)
        return math.sqrt(d_x + d_y + d_z)

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def get_z(self) -> float:
        return self.z

    def __str__(self):
        return "X: {X}, Y: {Y} , Z: {Z}".format(X=self.x, Y=self.y, Z=self.z)
