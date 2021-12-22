import unittest

from graph.Location import Location
from graph.Node import Node


class NodeTest(unittest.TestCase):
    n1 = Node(key=1, position=(1, 3, 0))
    n2 = Node(key=2, position=(2, 4, 0))
    n3 = Node(key=3, position=(1, 5, 0))
    n4 = Node(key=4, position=(3, 2, 0))
    n5 = Node(key=5, position=(0, 3, 0))
    node_list = [n1, n2, n3, n4, n5]

    def test_getKey(self):
        self.assertEqual(self.n1.getKey(), 1)
        self.assertEqual(self.n2.getKey(), 2)
        self.assertEqual(self.n3.getKey(), 3)
        self.assertEqual(self.n4.getKey(), 4)
        self.assertEqual(self.n5.getKey(), 5)

    def test_getPosition(self):
        self.assertEqual(self.n1.getPosition().__str__(), Location(1, 3, 0).__str__())
        self.assertEqual(self.n2.getPosition().__str__(), Location(2, 4, 0).__str__())
        self.assertEqual(self.n3.getPosition().__str__(), Location(1, 5, 0).__str__())
        self.assertEqual(self.n4.getPosition().__str__(), Location(3, 2, 0).__str__())
        self.assertEqual(self.n5.getPosition().__str__(), Location(0, 3, 0).__str__())

    def test_setPosition(self):
        coordinates = [5, 6, 0]
        self.n1.setPosition(coordinates)
        self.n2.setPosition(coordinates)
        self.n3.setPosition(coordinates)
        self.n4.setPosition(coordinates)
        self.n5.setPosition(coordinates)
        self.assertEqual(self.n1.getPosition().__str__(), Location(coordinates[0], coordinates[1], coordinates[2]).__str__())
        self.assertEqual(self.n2.getPosition().__str__(), Location(coordinates[0], coordinates[1], coordinates[2]).__str__())
        self.assertEqual(self.n3.getPosition().__str__(), Location(coordinates[0], coordinates[1], coordinates[2]).__str__())
        self.assertEqual(self.n4.getPosition().__str__(), Location(coordinates[0], coordinates[1], coordinates[2]).__str__())
        self.assertEqual(self.n5.getPosition().__str__(), Location(coordinates[0], coordinates[1], coordinates[2]).__str__())


if __name__ == '__main__':
    runner = unittest.main
    runner.runTests()

