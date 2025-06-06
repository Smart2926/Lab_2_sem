import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import prim_mst, edge_list

class TestGraphUtils(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]
        ]

    def test_edge_list(self):
        expected_edges = [
            (0, 1, 2), (0, 3, 6),
            (1, 2, 3), (1, 3, 8), (1, 4, 5),
            (2, 4, 7), (3, 4, 9)
        ]
        self.assertEqual(sorted(edge_list(self.matrix)), sorted(expected_edges))

    def test_prim_mst(self):
        total_weight, mst_edges = prim_mst(self.matrix)
        self.assertEqual(total_weight, 16)
        expected_mst_edges = [
            (0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)
        ]
        self.assertEqual(sorted(mst_edges), sorted(expected_mst_edges))

if __name__ == '__main__':
    unittest.main()
