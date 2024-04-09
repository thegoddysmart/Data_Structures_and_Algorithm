class ListDictionary:
    """
    Dictionary: An abstract data type representing a dictionary (key-value pairs).

    Attributes:
        _data (list of tuples): A list of tuples representing key-value pairs.
    """
    
    def __init__(self):
        """implement the constructor
        Initializes a new empty dictionary
        """
        self._data = []

    def insert(self, key, value):
        """
        Inserts a (key, value) pair into the dictionary.

        Args:
            key: The key to insert.
            value: The value to associate with the key.

        Returns:
            bool: True if the value already existed and was overwritten, False otherwise.
        """
        for i, (k, _) in enumerate(self._data):
            if k == key:
                self._data[i] = (key, value)
                return True
        self._data.append((key, value))
        return False

    # implementing the rest of the dictionary methods below
    def remove(self, key):
        """
        Removes a key-value pair from the dictionary.

        Args:
            key: The key to remove.

        Returns:
            bool: True if the key was found and removed, False otherwise.
        """
        for i, (k, _) in enumerate(self._data):
            if k == key:
                self._data.pop(i)
                return True
        return False
    
    def contains(self, key):
        """
        Checks if a key is present in the dictionary.

        Args:
            key: The key to check.

        Returns:
            bool: True if the key is present, False otherwise.
        """
        for k, _ in self._data:
            if k == key:
                return True
        return False
    
    def lookup(self, key):
        """
        Looks up the value associated with a key in the dictionary.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key, or None if the key is not present.
        """
        for k, v_list in self._data:
            if k == key:
                return v_list
        return None
    
    def get_keys(self):
        """
        Returns a list of all keys in the dictionary.

        Returns:
            list: A list of all keys in the dictionary.
        """
        return [k for k, _ in self._data]
    
    def get_values(self):
        """
        Returns a list of all values in the dictionary.

        Returns:
            list: A list of all values in the dictionary.
        """
        return [v for _, v in self._data]
    
    def size(self):
        """
        Returns the number of key-value pairs in the dictionary.

        Returns:
            int: The number of key-value pairs in the dictionary.
        """
        return len(self._data)