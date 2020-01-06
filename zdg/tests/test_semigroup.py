import unittest
from zdg.semigroup import reduce_poss_maps, get_semigroups
from zdg.groupoid import Groupoid as groid

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

class TestGetSemigroups(unittest.TestCase):

    def test_three(self):
        g = groid({1, 2, 3}, comm=True, zero=1)
        mappings = {
            frozenset({2, 3}): {2, 3},
            frozenset({2}): {2, 3},
            frozenset({3}): {2, 3}
        }
        semigroups = get_semigroups(mappings, g)
        self.assertIsNotNone(semigroups)
        for s in semigroups:
            self.assertIn(s.get(2, 3), {2, 3})

    def test_four(self):
        g = groid({0, 1, 2, 3}, comm=True, zero=0)
        g.set(1, 2, 0)
        g.set(2, 3, 0)
        mappings = {
            frozenset({1, 3}): {1, 2, 3},
            frozenset({1}): {1, 2, 3, 0},
            frozenset({2}): {1, 2, 3, 0},
            frozenset({3}): {1, 2, 3, 0},
        }

        semigroups = get_semigroups(mappings, g)
        self.assertIsNotNone(semigroups)
        for s in semigroups:
            self.assertIn(s.get(1, 3), {1, 2, 3})
