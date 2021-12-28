import copy

'''
A class to represent an Edge in a weighted directed graph
'''


class Edge:

    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight

    @classmethod
    def copyEdge(cls, edge):
        cls.src = copy.deepcopy(edge.src)
        cls.dest = copy.deepcopy(edge.dest)
        cls.weight = copy.deepcopy(edge.weight)

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getWeight(self):
        return self.weight

    def __str__(self):
        return "source: {SOURCE}, destination: {DESTINATION}, weight: {WEIGHT}".format(SOURCE=self.src,
                                                                                       DESTINATION=self.dest,
                                                                                       WEIGHT=self.weight)
