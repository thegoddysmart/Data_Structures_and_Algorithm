class Sort:
    def __init__(self):
        self.reset_stats()

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

    def swap(self, lst, i, j):
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
        self.moves += 3

    #
    # Task 1
    #

    def mystery_sort(self, lst):
        for i in range(len(lst) - 1, 0, -1):
            for j in range(len(lst) - 1, len(lst) - 1 - i, -1):
                if self.compare(lst[j] < lst[j - 1]):
                    self.swap(lst, j, j - 1)

    #
    # Task 2
    #

    # returns the nth digit of num,
    # where digit 0 is the least significant digit
    # e.g.: digit(1234, 0) -> 4
    def digit(num, n):
        return int(num // 10 ** n % 10)

    # returns a list of buckets of order radix
    # e.g.: get_new_buckets(10) will return a
    # 2D list of 10 empty lists: [ [], [], [], ... ]
    def get_new_buckets(radix):
        buckets = []
        for i in range(radix):
            buckets.append([])
        return buckets

    # get the maximum number of digits
    # among any number in the input list
    def get_max_num_digits(lst):
        # Task 2, Step 1
        return 0

    # converts a list of numbers to a list
    # of buckets, with entries sorted by
    # their least significant digit
    def list_to_buckets(self, lst):
        # Task 2, Step 2
        return None

    # converts a list of buckets
    # into a one-dimensional list
    def buckets_to_list(self, buckets):
        # Task 2, Step 3
        return None

    # sort a list of numbers by distributing
    # them to buckets according to their digits
    def radix_sort(self, lst):
        # Task 2, Step 4
        return None

