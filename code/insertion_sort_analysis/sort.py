import random

MAX_VAL = 65536

class Sort:
    def __init__(self):
        self.reset_stats()

    # construct a random list of size n
    def random_list(n):
        lst = []
        for i in range(n):
           lst.append(random.randint(0, MAX_VAL))
        return lst

    # construct an almost sorted list of size n
    def almost_sorted_list(n):
        # first get a random list of size n
        lst = Sort.random_list(n)

        # use Python's built-in list sorting algorithm
        lst.sort()

        # move one quarter of the elements out of
        # place by between 1 and 5 places
        for i in range(n // 8):
            j = random.randint(0, n - 1)
            displace = -5 + random.randint(0, 10)
            k = j + displace;
            if k < 0:
                k = 0;
            elif k > n - 1:
                k = n - 1

            temp = lst[j]
            lst[j] = lst[k]
            lst[k] = temp

        return lst

    def reset_stats(self):
        self.comps = 0
        self.moves = 0

    def get_comps(self):
        return self.comps

    def get_moves(self):
        return self.moves

    def compare(self, comparison):
        self.comps += 1
        return comparison

    # move val into the list at position idx
    def move(self, lst, idx, val):
        lst[idx] = val
        self.moves += 1

    def insertion_sort(self, lst):
        for i in range(1, len(lst)):
            to_insert = lst[i]
            j = i
            while j > 0 and self.compare(to_insert < lst[j - 1]):
                self.move(lst, j, lst[j - 1])
                j -= 1
            self.move(lst, j, to_insert)

if __name__ == "__main__":
    sort = Sort()

    print("insertion sort on a random list\n")
    lst = Sort.random_list(100)
    sort.insertion_sort(lst)
    print("comparisons: " + str(sort.get_comps()))
    print("moves: " + str(sort.get_moves()))
    sort.reset_stats()

    print("\n\n")

    print("insertion sort on an almost sorted list\n")
    lst = Sort.almost_sorted_list(100)
    sort.insertion_sort(lst)
    print("comparisons: " + str(sort.get_comps()))
    print("moves: " + str(sort.get_moves()))
    sort.reset_stats()