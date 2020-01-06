import unittest
from zdg.groupoid import Groupoid, is_assoc

class TestGroupoid(unittest.TestCase):

    def setUp(self):
        self.grpd = Groupoid((1, 2, 3), comm=False)
        self.grpd_assoc = Groupoid((1, 2, 3))

    def test_prod(self):
        self.assertEqual(self.grpd.get(1, 2), 0)
        self.grpd.set(1, 2, 3)
        self.assertEqual(self.grpd.get(1, 2), 3)
        self.assertEqual(self.grpd.get(2, 1), 0)

    def test_comm_prod(self):
        self.assertEqual(self.grpd_assoc.get(1, 2), 0)
        self.grpd_assoc.set(1, 2, 3)
        self.assertEqual(self.grpd_assoc.get(1, 2), 3)
        self.assertEqual(self.grpd_assoc.get(2, 1), 3)

    def test_square(self):
        self.assertEqual(self.grpd.get(1, 1), 0)
        self.grpd.set(1, 1, 2)
        self.assertEqual(self.grpd.get(1, 1), 2)

    def test_comm_square(self):
        self.assertEqual(self.grpd.get(1, 1), 0)
        self.grpd.set(1, 1, 2)
        self.assertEqual(self.grpd.get(1, 1), 2)

class TestIsAssoc(unittest.TestCase):

    def setUp(self):
        self.grpd = Groupoid((1, 2, 3), comm=False)
        self.grpd_comm = Groupoid((1, 2, 3))

    def test_assoc(self):
        self.assertTrue(is_assoc(self.grpd))
        self.assertTrue(is_assoc(self.grpd_comm))

    def test_assoc_comm(self):
        self.grpd_comm.set(1, 2, 3)
        self.grpd_comm.set(2, 3, 3)
        self.grpd_comm.set(1, 3, 3)
        self.grpd_comm.set(3, 3, 3)
        self.grpd_comm.set(1, 1, 1)
        self.grpd_comm.set(2, 2, 2)
        self.assertTrue(is_assoc(self.grpd_comm))

    def test_noassoc_comm(self):
        self.grpd_comm.set(1, 2, 3)
        self.grpd_comm.set(2, 3, 3)
        self.assertFalse(is_assoc(self.grpd_comm))
