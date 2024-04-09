class ListSet:
    def __init__(self):
        self.items = []

    def insert(self, item):
        if item in self.items:
            return False
        else:
            self.items.append(item)
            return True

    def contains(self, item):
        for i in self.items:
            if i == item:
                return True
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
