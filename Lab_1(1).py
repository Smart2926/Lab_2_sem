import unittest
from main import zigzag_traversal
class TestZigzagTraversal(unittest.TestCase):
    def test_5x5(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25]
        self.assertEqual(zigzag_traversal(matrix), expected)
    
    def test_2x4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(zigzag_traversal(matrix), expected)
    
    def test_1x6(self):
        matrix = [[1, 2, 3, 4, 5, 6]]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(zigzag_traversal(matrix), expected)
    
    def test_6x1(self):
        matrix = [[1], [2], [3], [4], [5], [6]]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(zigzag_traversal(matrix), expected)
    
    def test_1x1(self):
        matrix = [[1]]
        expected = [1]
        self.assertEqual(zigzag_traversal(matrix), expected)
    
unittest.main()