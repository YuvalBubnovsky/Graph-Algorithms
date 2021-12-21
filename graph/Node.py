import copy
from graph.Location import Location


class Node:
    def __init__(self, key, position: Location):
        self.key = key
        self.position = position.copyLoc(position)
        # self.tag = tag

    @classmethod
    def copyNode(cls, node):
        cls.key = copy.deepcopy(node.key)
        cls.position = copy.deepcopy(node.position)
        cls.tag = copy.deepcopy(node.tag)


    def getKey(self):
        return self.key

    def getPosition(self):
        return self.position

    def setPosition(self, coordinates: list):
        self.position = Location(coordinates[0], coordinates[1], coordinates[2])

    def getTag(self):
        return self.tag

    def setTag(self, newTag):
        self.tag = newTag
