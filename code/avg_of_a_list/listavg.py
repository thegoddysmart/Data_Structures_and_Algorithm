class ListAverage:
    def __init__(self, lst):
        self.lst = lst.copy()
        self.total = sum(lst) # Initialize the total sum of the list

    def add(self, num):
        self.lst.append(num)
        self.total += num # Update the total sum of the list

    def compute_avg(self):
        total = 0
        for num in self.lst:
            total += num
        return total / len(self.lst)

    def compute_avg_faster(self):
        return self.total / len(self.lst)