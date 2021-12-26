import unittest
from collections import defaultdict

from graph.DiGraph import DiGraph
from graph.Edge import Edge
from graph.GraphAlgo import GraphAlgo
from graph.Node import Node


class MyTestCase(unittest.TestCase):
    graphAlgo = GraphAlgo()
    graphAlgo.load_from_json(r"C:\Users\itama\PycharmProjects\OOP_2021_Ex3\data\A0.json")

    def test_load(self):
        self.assertTrue(self.graphAlgo.load_from_json(r"*\PycharmProjects\OOP_2021_Ex3\data\A0.json"))
        self.assertTrue(self.graphAlgo.graph.nodes.get(9))
        self.assertTrue(self.graphAlgo.graph.edges.get(7))
        self.assertTrue(self.graphAlgo.load_from_json(r"*\PycharmProjects\OOP_2021_Ex3\data\A1.json"))
        self.assertTrue(self.graphAlgo.graph.nodes.get(16))

    def test_save(self):
        self.assertTrue(self.graphAlgo.save_to_json(r"*\PycharmProjects\OOP_2021_Ex3\tests\test.json"))

    def test_transpose(self):
        transpose_dict = defaultdict(list)
        transpose_dict[0].append({1: 1.8884659521433524})
        transpose_dict[0].append({10: 1.1761238717867548})
        transpose_dict[1].append({0: 1.4004465106761335})
        transpose_dict[1].append({2: 1.7155926739282625})
        transpose_dict[2].append({1: 1.7646903245689283})
        transpose_dict[2].append({3: 1.0980094622804095})
        transpose_dict[3].append({2: 1.1435447583365383})
        transpose_dict[3].append({4: 1.4899867265011255})
        transpose_dict[4].append({3: 1.4301580756736283})
        transpose_dict[4].append({5: 1.4622464066335845})
        transpose_dict[5].append({4: 1.9442789961315767})
        transpose_dict[5].append({6: 1.6677173820549975})
        transpose_dict[6].append({5: 1.160662656360925})
        transpose_dict[6].append({7: 1.0176531013725074})
        transpose_dict[7].append({6: 1.3968360163668776})
        transpose_dict[7].append({8: 1.6449953452844968})
        transpose_dict[8].append({7: 1.354895648936991})
        transpose_dict[8].append({9: 1.4575484853801393})
        transpose_dict[9].append({8: 1.8526880332753517})
        transpose_dict[9].append({10: 1.0887225789883779})
        transpose_dict[10].append({0: 1.4620268165085584})
        transpose_dict[10].append({9: 1.022651770039933})
        self.assertEqual(transpose_dict, self.graphAlgo.transpose())

    def test_is_connected(self):
        self.assertTrue(self.graphAlgo.is_connected())
        n9 = Node(9, (1,1,0))
        n10 = Node(10, (2,2,2))
        n11 = Node(11, (3,3,3))
        e9 = Edge(9,10,2.3)
        e10 = Edge(9,11, 2.5)
        nodes = {9:(1,1,0),10:(2,2,2),11:(3,3,3)}
        edges = {9:[{10:2.3},{11:2.5}]}
        dgraph = DiGraph().init_graph(nodes=nodes, edges=edges)
        dgraphalgo = GraphAlgo.init_graph(dgraph)
        self.assertFalse(dgraphalgo.is_connected())

if __name__ == '__main__':
    runner = unittest.main()
    runner.runTests()
