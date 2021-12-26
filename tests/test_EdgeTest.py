import unittest
from graph.Edge import Edge
from graph.Node import Node
from graph.Location import Location


class MyTestCase(unittest.TestCase):
    n1 = Node(key=1, position=(1, 3, 0))
    n2 = Node(key=2, position=(2, 4, 0))
    n3 = Node(key=3, position=(1, 5, 0))
    n4 = Node(key=4, position=(3, 2, 0))
    n5 = Node(key=5, position=(0, 3, 0))

    e1 = Edge(src=n1.getKey(), dest=n2.getKey(), weight=0.265)
    e2 = Edge(src=n2.getKey(), dest=n4.getKey(), weight=0.564)
    e3 = Edge(src=n4.getKey(), dest=n5.getKey(), weight=1.26578)
    e4 = Edge(src=n5.getKey(), dest=n3.getKey(), weight=1.9852)
    e5 = Edge(src=n3.getKey(), dest=n1.getKey(), weight=0.65998)
    e6 = Edge(src=n1.getKey(), dest=n4.getKey(), weight=1.659874)

    def test_getSrc(self):
        self.assertEqual(self.e1.getSrc(), 1)
        self.assertEqual(self.e2.getSrc(), 2)
        self.assertEqual(self.e3.getSrc(), 4)
        self.assertEqual(self.e4.getSrc(), 5)
        self.assertEqual(self.e5.getSrc(), 3)
        self.assertEqual(self.e6.getSrc(), 1)

    def test_getDest(self):
        self.assertEqual(self.e1.getDest(), 2)
        self.assertEqual(self.e2.getDest(), 4)
        self.assertEqual(self.e3.getDest(), 5)
        self.assertEqual(self.e4.getDest(), 3)
        self.assertEqual(self.e5.getDest(), 1)
        self.assertEqual(self.e6.getDest(), 4)

    def test_getWeight(self):
        self.assertEqual(self.e1.getWeight(), 0.265)
        self.assertEqual(self.e2.getWeight(), 0.564)
        self.assertEqual(self.e3.getWeight(), 1.26578)
        self.assertEqual(self.e4.getWeight(), 1.9852)
        self.assertEqual(self.e5.getWeight(), 0.65998)
        self.assertEqual(self.e6.getWeight(), 1.659874)



if __name__ == '__main__':
    runner = unittest.main()
    runner.runTests()
