import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ijones import count_paths

class TestIJones(unittest.TestCase):

    def test_example1(self):
        grid = [
            list("aaa"),
            list("cab"),
            list("def")
        ]
        self.assertEqual(count_paths(grid), 4)

    def test_example2(self):
        grid = [
            list("abcdefaghi")
        ]
        self.assertEqual(count_paths(grid), 2)

    def test_example3(self):
        grid = [list("aaaaaaa") for _ in range(6)]
        self.assertEqual(count_paths(grid), 93312)

    def test_single_tile(self):
        grid = [list("a")]
        self.assertEqual(count_paths(grid), 2)

    def test_no_paths(self):
        grid = []
        self.assertEqual(count_paths(grid), 0)
    def test_example1(self):
        grid = [
            list("abc"),
            list("aac"),
            list("abb")
        ]
        self.assertEqual(count_paths(grid), 3)

unittest.main()