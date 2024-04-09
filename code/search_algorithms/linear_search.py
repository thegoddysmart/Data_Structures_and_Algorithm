def linear_search_v1(collection, target):
    """
    Perform linear search on the given collection to find the target element.
    
    Args:
        collection (list): The collection to search within.
        target: The target element to search for.
        
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for index in range(len(collection)):
        if collection[index] == target:
            return index
    return -1

def linear_search_v2(collection, target):
    """
    Perform linear search on the given collection to find the target element.
    
    Args:
        collection (list): The collection to search within.
        target: The target element to search for.
        
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    index = 0
    while index < len(collection):
        if collection[index] == target:
            return index
        index += 1
    return -1

def linear_search_v3(collection, target):
    """
    Perform linear search on the given collection to find the target element.
    
    Args:
        collection (list): The collection to search within.
        target: The target element to search for.
        
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for index, item in enumerate(collection):
        if item == target:
            return index
    return -1

def linear_search_sorted(collection, target):
    """
    Perform linear search on the given sorted collection to find the target element.
    If the collection is sorted, the search can stop early if an element greater
    than the target is encountered.
    
    Args:
        collection (list): The sorted collection to search within.
        target: The target element to search for.
        
    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for index, item in enumerate(collection):
        if item == target:
            return index
        elif item > target:
            # If the current item is greater than the target,
            # we can stop the search early as the target won't be found beyond this point
            return -1
    return -1
