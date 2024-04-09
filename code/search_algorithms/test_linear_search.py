import unittest
from linear_search import linear_search_v1, linear_search_v2, linear_search_v3, linear_search_sorted

class TestLinearSearch(unittest.TestCase):
    def test_linear_search_v1(self):
        # Test cases for linear_search_v1
        self.assertEqual(linear_search_v1([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(linear_search_v1([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(linear_search_v1([], 3), -1)
        self.assertEqual(linear_search_v1([5], 5), 0)

    def test_linear_search_v2(self):
        # Test cases for linear_search_v2
        self.assertEqual(linear_search_v2([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(linear_search_v2([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(linear_search_v2([], 3), -1)
        self.assertEqual(linear_search_v2([5], 5), 0)

    def test_linear_search_v3(self):
        # Test cases for linear_search_v3
        self.assertEqual(linear_search_v3([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(linear_search_v3([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(linear_search_v3([], 3), -1)
        self.assertEqual(linear_search_v3([5], 5), 0)

    def test_linear_search_sorted(self):
        # Test cases for linear_search_sorted
        self.assertEqual(linear_search_sorted([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(linear_search_sorted([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(linear_search_sorted([], 3), -1)
        self.assertEqual(linear_search_sorted([5], 5), 0)

if __name__ == '__main__':
    unittest.main()
