import unittest
from collections import defaultdict

from graph.DiGraph import DiGraph
from graph.Edge import Edge
from graph.GraphAlgo import GraphAlgo
from graph.Node import Node


class MyTestCase(unittest.TestCase):
    graphAlgo = GraphAlgo()
    graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A0.json")

    def test_load(self):
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A0.json"))
        self.assertTrue(self.graphAlgo.graph.nodes.get(9))
        self.assertTrue(self.graphAlgo.graph.edges.get(7))
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A1.json"))
        self.assertTrue(self.graphAlgo.graph.nodes.get(16))

    def test_save(self):
        self.assertTrue(self.graphAlgo.save_to_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\tests\test.json"))

    def test_is_connected(self):
        self.assertTrue(self.graphAlgo.is_connected())
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A0.json"))
        self.assertTrue(self.graphAlgo.is_connected())
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A2.json"))
        self.assertTrue(self.graphAlgo.is_connected())
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A3.json"))
        self.assertTrue(self.graphAlgo.is_connected())
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A4.json"))
        self.assertTrue(self.graphAlgo.is_connected())
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A5.json"))
        self.assertTrue(self.graphAlgo.is_connected())


if __name__ == '__main__':
    runner = unittest.main()
    runner.runTests()
