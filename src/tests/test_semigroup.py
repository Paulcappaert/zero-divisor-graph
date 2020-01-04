import unittest
from src.semigroup import reduce_poss_maps

class TestReduceMaps(unittest.TestCase):

    def setUp(self):
        self.p_maps = {
            frozenset({1, 2}): {2},
            frozenset({1}): {1, 2, 0},
            frozenset({2}): {1},
            frozenset({0}): {0},
            frozenset({0, 1}): {0},
            frozenset({0, 2}): {0}
        }
        self.elements = (0, 1, 2)

    def test_reduce1(self):
        reduce_poss_maps(self.p_maps, self.elements)
        self.assertEqual(self.p_maps[frozenset({1})], {1})
        self.assertEqual(self.p_maps[frozenset({2})], {1})
        self.assertEqual(self.p_maps[frozenset({1, 2})], {2})

    def test_reduce2(self):
        self.p_maps[frozenset({2})] = {0}
        reduce_poss_maps(self.p_maps, self.elements)
        self.assertEqual(self.p_maps[frozenset({1})], {1})
        self.assertEqual(self.p_maps[frozenset({2})], {0})
        self.assertEqual(self.p_maps[frozenset({1, 2})], {2})

    def test_reduce3(self):
        self.p_maps[frozenset({2})] = {2}
        reduce_poss_maps(self.p_maps, self.elements)
        self.assertEqual(self.p_maps[frozenset({1})], {1, 2})
        self.assertEqual(self.p_maps[frozenset({2})], {2})
        self.assertEqual(self.p_maps[frozenset({1, 2})], {2})
