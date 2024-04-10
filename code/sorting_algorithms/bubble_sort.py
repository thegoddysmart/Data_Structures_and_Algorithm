def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.
    
    Parameters:
    arr (list): The unsorted array to be sorted.
    
    Returns:
    list: The sorted array.
    """
    n = len(arr)
    
    # we are traversing through all elements in the array
    for i in range(n):
        for j in range(0, n-i-1):
            # if the element is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Usage
arr = [64, 34, 25, 12, 22, 11, 90, 75, 9, 89]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
