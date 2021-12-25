import unittest

from graph.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    graphAlgo = GraphAlgo()

    def test_load(self):
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A0.json"))
        self.assertTrue(self.graphAlgo.graph.nodes.get(9))
        self.assertTrue(self.graphAlgo.graph.edges.get(7))
        self.assertTrue(self.graphAlgo.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A1.json"))
        self.assertTrue(self.graphAlgo.graph.nodes.get(16))

    def test_save(self):
        self.assertTrue(self.graphAlgo.save_to_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\tests\test.json"))

    # TODO: add this test
    def test_transpose(self):
        pass


if __name__ == '__main__':
    unittest.main()
