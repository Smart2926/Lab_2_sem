import unittest
from main import BinaryTree, find_successor

class TestFindSuccessor(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(10)
        self.root.left = BinaryTree(5, parent=self.root)
        self.root.right = BinaryTree(15, parent=self.root)
        self.root.left.left = BinaryTree(3, parent=self.root.left)
        self.root.left.right = BinaryTree(7, parent=self.root.left)
        self.root.right.right = BinaryTree(20, parent=self.root.right)
        self.root.right.right.left = BinaryTree(12, parent=self.root.right.right)

    def test_successor(self):
        self.assertEqual(find_successor(self.root, self.root.left.right).value, 15)
        self.assertEqual(find_successor(self.root, self.root.left.left).value, 7)
        self.assertEqual(find_successor(self.root, self.root.left).value, 10)
        self.assertIsNone(find_successor(self.root, self.root.right.right))

unittest.main()
