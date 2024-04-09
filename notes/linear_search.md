# Linear Search

Linear search, also known as *sequential search*, is a straightforward searching algorithm that traverses a collection of elements sequentially until the desired item is found or the entire collection has been searched. It is one of the simplest and most intuitive searching algorithms.

## Algorithm Steps:
- Start: Begin at the first element of the collection.

- Iterate: Traverse each element in the collection sequentially.

- Compare: Compare the current element with the target element.

- Found: If the current element matches the target, return its index.

- Not Found: If the target element is not found after traversing the entire collection, return a special value (e.g., -1) to indicate that the element is not present.

Pseudocode:
``` plaintext
function linear_search(collection, target):
    for index from 0 to length(collection) - 1:
        if collection[index] equals target:
            return index
    return -1
```

### Example:
Suppose we have an array of integers: [5, 8, 3, 12, 7, 10] and we want to search for the target element 12.

- Start: Begin at the first element 5.
- Iterate: Traverse each element sequentially.
- Compare: Compare each element with the target (12).
- Found: When reaching the element 12, return its index (3).
- Not Found: If the entire collection is searched and the target is not found, return -1.


## Time Complexity:
- **Best Case: O(1)** - When the target element is found at the first position.

- **Worst Case: O(n)** - When the target element is located at the end of the collection or is not present at all.

- **Average Case: O(n/2) = O(n)** - On average, linear search examines half of the elements in the collection.


## Space Complexity:
Linear search has a space complexity of `O(1)` because it only requires a constant amount of extra space for storing loop indices and temporary variables.


## Considerations:
- Linear search is suitable for small collections or unsorted data.
- It is inefficient for large collections or when performance is critical.
- Linear search is easy to implement and understand, making it useful for educational purposes and simple applications.





