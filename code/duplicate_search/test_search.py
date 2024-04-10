import unittest
from search import Search 

class TestSearch(unittest.TestCase):
    def test_linear_no_dupes(self):
        search = Search([1, 2, 3])
        assert search.duplicate_count_linear(2) == 0

    def test_linear_one_dupe(self):
        search = Search([1, 2, 2, 3])
        assert search.duplicate_count_linear(2) == 1

    def test_linear_many_dupes(self):
        search = Search([1, 2, 2, 2, 2, 2, 2, 3])
        assert search.duplicate_count_linear(2) == 5

    def test_linear_dupe_at_start(self):
        search = Search([1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3])
        assert search.duplicate_count_linear(1) == 3

    def test_linear_dupe_at_end(self):
        search = Search([1, 2, 2, 2, 2, 2, 2, 3, 3, 3])
        assert search.duplicate_count_linear(3) == 2

    # add more unit tests for binary search below
    def test_binary_no_dupe(self):
        search = Search([1, 2, 3])
        assert search.duplicate_count_binary(2) == 0
        
    def test_binary_no_dupes(self):
        search = Search([1, 2, 3])
        assert search.duplicate_count_binary(2) == 0

    def test_binary_one_dupe(self):
        search = Search([1, 2, 2, 3])
        assert search.duplicate_count_binary(2) == 1

    def test_binary_many_dupes(self):
        search = Search([1, 2, 2, 2, 2, 2, 2, 3])
        assert search.duplicate_count_binary(2) == 5

    def test_binary_dupe_at_start(self):
        search = Search([1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3])
        assert search.duplicate_count_binary(1) == 3

    def test_binary_dupe_at_end(self):
        search = Search([1, 2, 2, 2, 2, 2, 2, 3, 3, 3])
        assert search.duplicate_count_binary(3) == 2

if __name__ == '__main__':
    unittest.main()