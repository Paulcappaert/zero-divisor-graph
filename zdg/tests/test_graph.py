import unittest
from zdg.graph import graph_from_edges, poss_mappings

class TestGraphFromEdges(unittest.TestCase):

    def test_neighborhood(self):
        G = graph_from_edges((1, 2))
        self.assertEqual(G[1], {2})
        self.assertEqual(G[2], {1})

    def test_neighborhood1(self):
        G = graph_from_edges((1, 2), (2, 3))
        self.assertEqual(G[1], {2})
        self.assertEqual(G[2], {1, 3})
        self.assertEqual(G[3], {2})

    def test_neighborhood2(self):
        G = graph_from_edges((1, 2), (2, 3), (3, 4), (4, 1))
        self.assertEqual(G[1], {2, 4})
        self.assertEqual(G[2], {1, 3})
        self.assertEqual(G[3], {2, 4})
        self.assertEqual(G[4], {1, 3})

    def test_neighborhood3(self):
        G = graph_from_edges((1, 2), (1, 3), (1, 4))
        self.assertEqual(G[1], {2, 3, 4})
        self.assertEqual(G[2], {1})
        self.assertEqual(G[3], {1})
        self.assertEqual(G[4], {1})

class TestPossMappings(unittest.TestCase):

    def test_poss1(self):
        poss, maps = poss_mappings(graph_from_edges((1, 2), (2, 3)))
        self.assertTrue(poss)
        self.assertEqual(maps[frozenset({1, 3})], {1, 2, 3})
        self.assertEqual(maps[frozenset({1})], {1, 2, 3, 0})
        self.assertEqual(maps[frozenset({2})], {2, 0})
        self.assertEqual(maps[frozenset({3})], {1, 2, 3, 0})

    def test_poss2(self):
        poss, maps = poss_mappings(graph_from_edges(
        (1, 2), (2, 3), (3, 4)))
        self.assertTrue(poss)
        self.assertEqual(maps[frozenset({1, 4})], {2, 3})
        self.assertEqual(maps[frozenset({2, 4})], {2})
        self.assertEqual(maps[frozenset({1, 3})], {3})
        self.assertEqual(maps[frozenset({1})], {1, 2, 3, 0})
        self.assertEqual(maps[frozenset({2})], {2, 0})
        self.assertEqual(maps[frozenset({3})], {3, 0})
        self.assertEqual(maps[frozenset({4})], {4, 3, 2, 0})


    def test_impossible(self):
        poss, maps = poss_mappings(graph_from_edges((1, 2), (3, 4)))
        self.assertFalse(poss)
        self.assertEqual(maps[frozenset({1, 3})], set())
        self.assertEqual(maps[frozenset({2, 4})], set())
        self.assertEqual(maps[frozenset({1, 4})], set())
        self.assertEqual(maps[frozenset({2, 3})], set())
