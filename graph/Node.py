import copy
from graph.Location import Location


class Node:
    def __init__(self, key, position: tuple):
        self.key = key
        # self.position = position.copyLoc(position)
        # self.tag = tag
        pos_location = Location(position[0], position[1], position[2])
        self.position = Location(pos_location.get_x(), pos_location.get_y(), pos_location.get_z())

    @classmethod
    def copyNode(cls, node):
        cls.key = copy.deepcopy(node.key)
        cls.position = copy.deepcopy(node.position)
        cls.tag = copy.deepcopy(node.tag)

    def getKey(self):
        return self.key

    def getPosition(self) -> Location:
        return self.position

    def setPosition(self, coordinates: list):
        self.position = Location(coordinates[0], coordinates[1], coordinates[2])

    def getTag(self):
        return self.tag

    def setTag(self, newTag):
        self.tag = newTag

    def get_x(self) -> float:
        return self.position.get_x()

    def get_y(self) -> float:
        return self.position.get_y()

    def get_z(self) -> float:
        return self.position.get_z()

    def __str__(self):
        return "key: {KEY}, position: {POSITION}".format(KEY=self.key, POSITION=self.position)
