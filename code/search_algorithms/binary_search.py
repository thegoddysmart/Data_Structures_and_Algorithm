def binary_search_iterative(arr, target):
    """
    Perform binary search on a sorted array in an iterative manner.

    Parameters:
    arr (list): The sorted array to search in.
    target: The element to search for.

    Returns:
    int: The index of the target element in the array if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    """
    Perform binary search on a sorted array in a recursive manner.

    Parameters:
    arr (list): The sorted array to search in.
    target: The element to search for.
    left (int): The left index of the search interval.
    right (int): The right index of the search interval.

    Returns:
    int: The index of the target element in the array if found, otherwise -1.
    """
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return -1

def binary_search(arr, target):
    """
    Wrapper function to initiate recursive binary search.

    Parameters:
    arr (list): The sorted array to search in.
    target: The element to search for.

    Returns:
    int: The index of the target element in the array if found, otherwise -1.
    """
    return binary_search_recursive(arr, target, 0, len(arr) - 1)
