import unittest
from binary_search import binary_search_iterative, binary_search_recursive

class TestBinarySearch(unittest.TestCase):

    def test_binary_search_iterative(self):
        arr = [1, 3, 5, 7, 9, 11, 13]
        self.assertEqual(binary_search_iterative(arr, 5), 2)
        self.assertEqual(binary_search_iterative(arr, 13), 6)
        self.assertEqual(binary_search_iterative(arr, 2), -1)

    def test_binary_search_recursive(self):
        arr = [1, 3, 5, 7, 9, 11, 13]
        self.assertEqual(binary_search_recursive(arr, 5, 0, len(arr) - 1), 2)
        self.assertEqual(binary_search_recursive(arr, 13, 0, len(arr) - 1), 6)
        self.assertEqual(binary_search_recursive(arr, 2, 0, len(arr) - 1), -1)

if __name__ == '__main__':
    unittest.main()
