import unittest

from graph.DiGraph import DiGraph
from graph.Edge import Edge
from graph.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    graph = DiGraph()

    for i in range(4):
        graph.add_node(node_id=i)
    graph.add_node(node_id=4, pos=(1, 3, 0))

    e1 = Edge(src=0, dest=1, weight=0.265)
    graph.add_edge(id1=e1.src, id2=e1.dest, weight=e1.weight)
    e2 = Edge(src=1, dest=3, weight=0.564)
    graph.add_edge(id1=e2.src, id2=e2.dest, weight=e2.weight)
    e3 = Edge(src=3, dest=4, weight=1.26578)
    graph.add_edge(id1=e3.src, id2=e3.dest, weight=e3.weight)
    e4 = Edge(src=2, dest=3, weight=1.9852)
    graph.add_edge(id1=e4.src, id2=e4.dest, weight=e4.weight)
    e5 = Edge(src=2, dest=1, weight=0.65998)
    graph.add_edge(id1=e5.src, id2=e5.dest, weight=e5.weight)
    e6 = Edge(src=0, dest=2, weight=1.659874)
    graph.add_edge(id1=e6.src, id2=e6.dest, weight=e6.weight)

    graphAlgo = GraphAlgo()



if __name__ == '__main__':
    runner = unittest.main
    runner.runTests()
