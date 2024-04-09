import unittest
from listavg import ListAverage

class TestListAverage(unittest.TestCase):
    def test(self):
        lavg = ListAverage([1, 2, 3])
        assert lavg.compute_avg() == 2.0

    def test_compute_avg(self):
        # Test the compute_avg method
        self.assertEqual(ListAverage([1, 2, 3]).compute_avg(), 2.0)
        
    def test_compute_avg_faster(self):
        # Test the compute_avg_faster method
        self.assertEqual(ListAverage([1, 2, 3, 4]).compute_avg_faster(), 2.5)
        
if __name__ == '__main__':
    unittest.main()