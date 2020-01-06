import unittest
from zdg.counter import ModularCounter as mc

class TestModularCounter(unittest.TestCase):

    def setUp(self):
        mods = [2, 3, 1]
        elements = ['a', 'b', 'c']
        self.ctr = mc(mods, elements)

    def test_initial(self):
        self.assertEqual(self.ctr.get_count('a'), 0)
        self.assertEqual(self.ctr.get_count('b'), 0)
        self.assertEqual(self.ctr.get_count('c'), 0)

    def test_oneTick(self):
        self.ctr.tick()
        self.assertEqual(self.ctr.get_count('a'), 1)
        self.assertEqual(self.ctr.get_count('b'), 0)
        self.assertEqual(self.ctr.get_count('c'), 0)

    def test_ThreeTick(self):
        for i in range(3):
            self.ctr.tick()
        self.assertEqual(self.ctr.get_count('a'), 1)
        self.assertEqual(self.ctr.get_count('b'), 1)
        self.assertEqual(self.ctr.get_count('c'), 0)

    def test_SixTick(self):
        for i in range(6):
            self.ctr.tick()
        self.assertEqual(self.ctr.get_count('a'), 0)
        self.assertEqual(self.ctr.get_count('b'), 0)
        self.assertEqual(self.ctr.get_count('c'), 0)

    def test_SevenTick(self):
        for i in range(7):
            self.ctr.tick()
        self.assertEqual(self.ctr.get_count('a'), 1)
        self.assertEqual(self.ctr.get_count('b'), 0)
        self.assertEqual(self.ctr.get_count('c'), 0)
