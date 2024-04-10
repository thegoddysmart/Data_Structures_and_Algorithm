class Search:
    def __init__(self, lst):
        self.lst = lst 

    def duplicate_count_linear(self, num):
        total = 0
        for val in self.lst:
            if val == num:
                total += 1

        if total == 0:
            return 0
        else:
            # number of duplicates is number of occurrences - 1
            return total - 1

    def duplicate_count_binary(self, num):
        # implementing the binary search duplicate count here
        left = 0
        right = len(self.lst) - 1
        index = -1
        
        while left <+ right:
            mid = (left + right) // 2
            if self.lst[mid] == num:
                index = mid
                break
            elif self.lst[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
                
        if index == -1:
            # number not found
            return 0
        
        # linear search to fund the number of duplicates to the left
        left_dup = 0
        i = index - 1
        while i >= 0 and self.lst[i] == num:
            left_dup += 1
            i -= 1
            
        # linear search to find the number of duplicates to the right
        right_dup = 0
        j = index + 1
        while j < len(self.lst) and self.lst[j] == num:
            right_dup += 1
            j += 1
        
        total_dup = left_dup + right_dup
        
        return total_dup       
