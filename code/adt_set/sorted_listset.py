class SortedListSet:
    def __init__(self):
        self.items = []

    def insert(self, item):
        # checking if the item already exists in the set
        if item in self.items:
            return False
        
        # Find the index where the new item should be inserted
        index = 0
        while index < len(self.items) and self.items[index] < item:
            index += 1
            
        # Insert the new item into the list
        self.items = self.items[:index] + [item] + self.items[index:]
        return True

    def contains(self, item):
        left, right = 0, len(self.items) - 1
        while left <+ right:
            mid = (left + right) // 2
            if self.items[mid] == item:
                return True
            elif self.items[mid] < item:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def delete(self, item):
        if item not in self.items:
            return False

        self.items.remove(item)
        return True

    def size(self):
        return len(self.items)

    def to_list(self):
        return self.items.copy()
