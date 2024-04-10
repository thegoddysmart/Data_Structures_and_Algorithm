# Insertion Sort

Insertion Sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is similar to how people sort a hand of playing cards. The algorithm iterates over the list, removing one element at a time and finding the correct position to insert it into the sorted part of the list.

Here are the steps of insertion sort:

1. Start with the element at index 1. Compare the element with all elements to its left (in this case, just the element at index 0). If the element at index 1 is less than the element at index 0, then slide the element at index 1 over so that the elements have switched places. The first two elements of the list are now sorted with respect to each other.

2. Consider the element at index 2. Again compare it with all elements to its left, sliding it over as necessary to maintain sortedness among the first three elements in the list. The first three elements of the list are now sorted with respect to each other.

3. Continue throughout the length of the list, taking one element at a time and finding its appropriate place in the sorted part of the list. During some iterations, an element may not need to be pushed left at all (if it is greater than the first element to its left).