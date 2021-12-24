import unittest

from graph.Location import Location


class MyTestCase(unittest.TestCase):
    l1 = Location(1,2.3545,0)
    l2 = Location(5.215,3,0)
    l3 = Location(1,2,0)
    l4 = Location(0.2315,0.9845,0)
    l5 = Location(1.54848,1.279135,0)

    def test_get_x(self):
        self.assertEqual(self.l1.get_x(), 1)
        self.assertEqual(self.l2.get_x(), 5.215)
        self.assertEqual(self.l3.get_x(), 1)
        self.assertEqual(self.l4.get_x(), 0.2315)
        self.assertEqual(self.l5.get_x(), 1.54848)

    def test_get_y(self):
        self.assertEqual(self.l1.get_y(), 2.3545)
        self.assertEqual(self.l2.get_y(), 3)
        self.assertEqual(self.l3.get_y(), 2)
        self.assertEqual(self.l4.get_y(), 0.9845)
        self.assertEqual(self.l5.get_y(), 01.279135)

    def test_get_z(self):
        # all should be 0
        self.assertEqual(self.l1.get_z(), 0)
        self.assertEqual(self.l2.get_z(), 0)
        self.assertEqual(self.l3.get_z(), 0)
        self.assertEqual(self.l4.get_z(), 0)
        self.assertEqual(self.l5.get_z(), 0)

    def test_distance(self):
        self.assertEqual(Location.distance(location1=self.l1, location2=self.l2), 4.264140622681198)
        self.assertEqual(Location.distance(location1=self.l1, location2=self.l3), 0.3544999999999998)
        self.assertEqual(Location.distance(location1=self.l1, location2=self.l4), 1.5708253403863839)
        self.assertEqual(Location.distance(location1=self.l1, location2=self.l5), 1.2071620411630744)
        self.assertEqual(Location.distance(location1=self.l2, location2=self.l3), 4.3320001154201275)
        self.assertEqual(Location.distance(location1=self.l2, location2=self.l4), 5.375640659493527)
        self.assertEqual(Location.distance(location1=self.l2, location2=self.l5), 4.050277182937607)
        self.assertEqual(Location.distance(location1=self.l3, location2=self.l4), 1.2735118766623261)
        self.assertEqual(Location.distance(location1=self.l3, location2=self.l5), 0.9058016662741354)
        self.assertEqual(Location.distance(location1=self.l4, location2=self.l5), 1.3495355140288083)


if __name__ == '__main__':
    runner = unittest.main()
    runner.runTests()
