import copy
from graph import Location


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

    def setPosition(self, coordinates):
        self.position = coordinates

    def getTag(self):
        return self.tag

    def setTag(self, newTag):
        self.tag = newTag
