def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of digits at specified position
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Update count to store actual position of digits in output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_value = max(arr)
    exp = 1

    # Perform counting sort for each digit, starting from least significant
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def num_dups_1(lst):
    """
    Practice One
    Deriving big-O running time.
    
    This algorithm looks at every element of the list and considers all elements to its right. 
    
    If it finds a duplicate, it adds one to the count. To avoid double-counting duplicates, it will break the inner loop once a duplicate is found and continue on to the next element of the outer loop.
    
    Returns:
    number of duplicates in a list
    """
    num_dup = 0
    
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                num_dup += 1
                break    # break out of the inner loop
            
    return num_dup

def num_dups_2(lst):
    radix_sort(lst)
    num_dups = 0
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            num_dups += 1
    return num_dups

# Usage
lst = [4, 1, 9, 1, 1, 4, 6, 8]
test_1 = num_dups_1(lst)
print("The number of duplicates for test 1 is: ", test_1) 

test_2 = num_dups_2(lst)
print("The number of duplicates for test 2 is: ", test_2) 


# The time complexity for the first algorithm is O(n^2) because it has two nested loops.
# The space complexity for the first algorithm is O(1) because it only uses a constant amount of space.

# The time complexity for the second algorithm is O(n*m) because it uses radix sort, which has a time complexity of O(n*m). The loop that follows the sorting has a time complexity of O(n).
# The space complexity for the second algorithm is O(n) because it uses a list(bucket) to store the sorted elements.

# So clearly we see the trade-off between time and space complexity. The first algorithm has a better space complexity but a worse time complexity, while the second algorithm has a better time complexity but a worse space complexity.