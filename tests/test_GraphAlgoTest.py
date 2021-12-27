import copy
import unittest
from collections import defaultdict

from graph.DiGraph import DiGraph
from graph.Edge import Edge
from graph.GraphAlgo import GraphAlgo
from graph.Node import Node


class MyTestCase(unittest.TestCase):
    graphAlgo = GraphAlgo()
    graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A0.json")

    def test_center(self):
        self.assertEqual((7, 6.806805834715163), self.graphAlgo.centerPoint())

    def test_load(self):
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A0.json"))
        self.assertTrue(self.graphAlgo.graph.nodes.get(9))
        self.assertTrue(self.graphAlgo.graph.edges.get(7))
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A1.json"))
        self.assertEqual((8, 9.925289024973141), self.graphAlgo.centerPoint())
        self.assertTrue(self.graphAlgo.graph.nodes.get(16))

    def test_save(self):
        self.assertTrue(self.graphAlgo.save_to_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\tests\test.json"))

    def test_center_connected(self):
        self.assertTrue(self.graphAlgo.is_connected())
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A0.json"))
        self.assertTrue(self.graphAlgo.is_connected())
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A2.json"))
        self.assertEqual((0, 7.819910602212574), self.graphAlgo.centerPoint())
        self.assertTrue(self.graphAlgo.is_connected())
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A3.json"))
        self.assertEqual((2, 8.182236568942237), self.graphAlgo.centerPoint())
        self.assertTrue(self.graphAlgo.is_connected())
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A4.json"))
        self.assertEqual((6, 8.071366078651435), self.graphAlgo.centerPoint())
        self.assertTrue(self.graphAlgo.is_connected())
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A5.json"))
        self.assertEqual((40, 9.291743173960954), self.graphAlgo.centerPoint())
        self.assertTrue(self.graphAlgo.is_connected())

    def test_tsp(self):
        self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A1.json")
        cities = [3, 2, 14, 5, 11, 10, 4]
        check = copy.deepcopy(cities)
        tsp = self.graphAlgo.TSP(cities)[0]
        shouldbe = [3, 4, 5, 6, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.assertListEqual(shouldbe, tsp)

    def test_shortest_path(self):

