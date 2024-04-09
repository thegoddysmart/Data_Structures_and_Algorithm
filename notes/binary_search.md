# Binary Search

Binary search is a highly efficient searching algorithm used to find a target value within a sorted array or list. It works by repeatedly dividing the search interval in half until the target element is found or the search interval is empty.


## Algorithm Steps:
- Start: Begin with the entire sorted array.
- Set Boundaries: Define two pointers, left and right, representing the start and end indices of the search interval, respectively.
- Middle Element: Calculate the middle index (mid) of the search interval.
- Compare: Compare the target element with the middle element.
- Found: If the target matches the middle element, return its index.
- Update Boundaries: If the target is less than the middle element, adjust the right pointer to mid - 1 to search the left half of the array. If the target is greater, adjust the left pointer to mid + 1 to search the right half.
- Repeat: Continue dividing the search interval in half until the target is found or the search interval is empty.


### Pseudocode:
```plaintext
function binary_search(sorted_array, target):
    left = 0
    right = length(sorted_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] equals target:
            return mid
        else if sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Example:
Suppose we have a sorted array of integers: [3, 6, 8, 12, 15, 21, 24] and we want to search for the target element 15.

- Start: Initially, left = 0 and right = 6, covering the entire array.
- Middle Element: Calculate mid = (0 + 6) // 2 = 3, pointing to the middle element 12.
- Compare: Compare 12 with the target 15.
- Update Boundaries: Since 15 is greater than 12, set left = 4 to search the right half.
Middle Element: Calculate mid = (4 + 6) // 2 = 5, pointing to the middle element 21.
- Compare: Compare 21 with the target 15.
- Update Boundaries: Since 15 is less than 21, set right = 4 to search the left half.
- Middle Element: Calculate mid = (4 + 4) // 2 = 4, pointing to the middle element 15.
- Compare: The target 15 matches the middle element 15. Return the index 4.


## Time Complexity:
- **Best Case: `O(1)`** - When the target element is found at the middle of the array.
- **Worst Case: `O(log n)`** - When the target element is not present or located at the extreme ends of the array.
- **Average Case: `O(log n)`** - On average, binary search halves the search interval in each step.


## Space Complexity:
Binary search has a space complexity of `O(1)` because it only requires a constant amount of extra space for storing loop indices and temporary variables.


## Considerations:
- Binary search is applicable only to sorted collections.
- It is significantly faster than linear search for large sorted collections.
- Binary search is widely used in various applications, including searching in databases, libraries, and data structures like trees and heaps.