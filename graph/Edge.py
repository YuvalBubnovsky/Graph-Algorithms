import copy

class Edge:

    def __init__(self, src, dest, weight, tag):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.tag = tag

    @classmethod
    def copyEdge(cls, edge):
        cls.src = copy.deepcopy(edge.src)
        cls.dest = copy.deepcopy(edge.dest)
        cls.weight = copy.deepcopy(edge.weight)
        cls.tag = copy.deepcopy(edge.tag)

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getWeight(self):
        return self.weight

    def getTag(self):
        return self.tag

    def setTag(self, newTag):
        self.tag = newTag