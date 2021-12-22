import copy
from graph.Location import Location


class Node:
    def __init__(self, key, position: Location):
        self.key = key
        # self.position = position.copyLoc(position)
        # self.tag = tag
        self.position = Location(position.get_x(), position.get_y(), position.get_z())

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

    def __str__(self):
        return "key: {KEY}, position: {POSITION}".format(KEY=self.key, POSITION=self.position)
