import unittest
from main_exercises import find_unsorted_subarrays

class TestFindUnsortedSubarray(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(find_unsorted_subarrays([1, 2, 3, 4, 5]), (-1, -1))
    
    def test_full_unsorted_array(self):
        self.assertEqual(find_unsorted_subarrays([5, 4, 3, 2, 1]), [(0, 4)])
    
    def test_single_element_array(self):
        self.assertEqual(find_unsorted_subarrays([42]), (-1, -1))
    
    def test_partial_unsorted_array(self):
        self.assertEqual(find_unsorted_subarrays([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]),  [(5, 6), (7, 8)])
    
    def test_unsorted_middle_segment(self):
        self.assertEqual(find_unsorted_subarrays([1, 3, 5, 8, 6, 7, 12, 14]), (3, 5))
   
    def test_unsorted_middle_segment(self):
        self.assertEqual(find_unsorted_subarrays([1, 2, 3, 6, 5, 4, 7, 8, 10, 9, 11]), [(3, 4), (8, 9)])

unittest.main()
