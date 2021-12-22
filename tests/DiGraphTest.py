import unittest

from graph.DiGraph import diGraph
from graph.Edge import Edge
from graph.Node import Node


class MyTestCase(unittest.TestCase):
    """add_node and add_edge are being tested when initializing the graph- if other
        methods work well, it means that those methods work as well"""

    graph = diGraph()

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

    # edge_list = [e1, e2, e3, e4, e5, e6]
    # for edge in edge_list:
    #     graph.add_edge(id1=edge.src, id2=edge.dest, weight=edge.weight)

    def test_v_size(self):
        self.assertEqual(self.graph.v_size(), 5)

    def test_e_size(self):
        self.assertEqual(self.graph.e_size(), 6)

    def test_get_all_v(self):
        graph_v = self.graph.get_all_v()
        print(graph_v.__str__())
        should_be = {0: self.graph.nodes.get(0), 1: self.graph.nodes.get(1), 2: self.graph.nodes.get(2),
                     3: self.graph.nodes.get(3), 4: self.graph.nodes.get(4)}
        print(should_be.__str__())
        self.assertDictEqual(graph_v, should_be)

    def test_all_in_edges_of_node(self):
        all_in_n0 = {}
        all_in_n1 = {0: self.e1.getWeight(), 2: self.e5.getWeight()}
        all_in_n2 = {0: self.e6.getWeight()}
        all_in_n3 = {1: self.e2.getWeight(), 2: self.e4.getWeight()}

        all_in_n4 = {3: self.e3.getWeight()}
        should_be_n0 = self.graph.all_in_edges_of_node(0)
        self.assertEqual(should_be_n0, all_in_n0)
        should_be_n1 = self.graph.all_in_edges_of_node(1)
        self.assertEqual(should_be_n1, all_in_n1)
        should_be_n2 = self.graph.all_in_edges_of_node(2)
        self.assertEqual(should_be_n2, all_in_n2)
        should_be_n3 = self.graph.all_in_edges_of_node(3)
        self.assertEqual(should_be_n3, all_in_n3)
        should_be_n4 = self.graph.all_in_edges_of_node(4)
        self.assertEqual(should_be_n4, all_in_n4)

    def test_all_out_edges_of_node(self):
        all_out_0 = {1: self.e1.getWeight(), 2: self.e6.getWeight()}
        all_out_1 = {3: self.e2.getWeight()}
        all_out_2 = {3: self.e4.getWeight(), 1: self.e5.getWeight()}
        all_out_3 = {4: self.e3.getWeight()}
        all_out_4 = {}

        should_be_0 = self.graph.all_out_edges_of_node(0)
        self.assertEqual(should_be_0, all_out_0)
        should_be_1 = self.graph.all_out_edges_of_node(1)
        self.assertEqual(should_be_1, all_out_1)
        should_be_2 = self.graph.all_out_edges_of_node(2)
        self.assertEqual(should_be_2, all_out_2)
        should_be_3 = self.graph.all_out_edges_of_node(3)
        self.assertEqual(should_be_3, all_out_3)
        should_be_4 = self.graph.all_out_edges_of_node(4)
        self.assertEqual(should_be_4, all_out_4)

    def test_remove_node(self):
        self.graph.remove_node(0)
        self.assertEqual(self.graph.node_counter, 4)
        nodes_after_remove = {1: self.graph.nodes.get(1), 2: self.graph.nodes.get(2), 3: self.graph.nodes.get(3),
                              4: self.graph.nodes.get(4)}
        self.assertEqual(nodes_after_remove, self.graph.get_all_v())
        self.assertEqual(self.graph.edge_counter, 4)  # testing help methods of remove_node

    def test_remove_edge(self):
        self.graph.remove_edge(node_id1=2, node_id2=1)
        self.assertEqual(self.graph.edge_counter, 5)

if __name__ == '__main__':
    runner = unittest.main()
    runner.runTests()
