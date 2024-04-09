import unittest
from listdict import ListDictionary

class TestListDictionary(unittest.TestCase):
    def test_insert(self):
        ldict = ListDictionary()
        # insert() should return false if not
        # overwriting a key
        assert not ldict.insert(1, "hello")

    # add more unit tests below
    def test_remove(self):
        ldict = ListDictionary()
        # Remove a key-value pair that doesn't exist
        self.assertFalse(ldict.remove(1))
        # Insert a key-value pair
        ldict.insert(1, "hello")
        # Remove the key-value pair
        self.assertTrue(ldict.remove(1))
        # Check that the key-value pair is removed
        self.assertIsNone(ldict.lookup(1))
        
    def test_contains(self):
        ldict = ListDictionary()
        # Check if a key is present in an empty dictionary
        self.assertFalse(ldict.contains(1))
        # Insert a key-value pair
        ldict.insert(1, "hello")
        # Check if the key is present
        self.assertTrue(ldict.contains(1))
        # Check if a key that doesn't exist is present
        self.assertFalse(ldict.contains(2))
        
    def test_lookup(self):
        ldict = ListDictionary()
        # Look up a key that doesn't exist
        self.assertIsNone(ldict.lookup(1))
        # Insert a key-value pair
        ldict.insert(1, "hello")
        # Look up the key
        self.assertEqual(ldict.lookup(1), "hello")
        # Insert a new key-value pair
        ldict.insert(2, "world")
        # Look up the new key
        self.assertEqual(ldict.lookup(2), "world")
        
    def test_get_keys(self):
        ldict = ListDictionary()
        # Get keys from an empty dictionary
        self.assertEqual(ldict.get_keys(), [])
        # Insert a key-value pair
        ldict.insert(1, "hello")
        # Get the keys
        self.assertEqual(ldict.get_keys(), [1])
        # Insert a new key-value pair
        ldict.insert(2, "world")
        # Get the keys
        self.assertEqual(ldict.get_keys(), [1, 2])
        
    def test_get_values(self):
        ldict = ListDictionary()
        # Checks if getting values from an empty dictionary returns an empty list
        self.assertEqual(ldict.get_values(), [])
        # Insert key-value pairs
        ldict.insert(1, "hello")
        ldict.insert(2, "world")
        # Get the values
        self.assertEqual(ldict.get_values(), ["hello", "world"])
        
    def test_size(self):
        ldict = ListDictionary()
        # check if the size of an empty dictionary is 0
        self.assertEqual(ldict.size(), 0)
        # Insert key-value pairs
        ldict.insert(1, "hello")
        ldict.insert(2, "world")
        ldict.insert(3, "!")
        # Check if the size of the dictionary is correct
        self.assertEqual(ldict.size(), 3)
        
if __name__ == '__main__':
    unittest.main()