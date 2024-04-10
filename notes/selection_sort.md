# Selection Sort

Selection Sort is another simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning. The algorithm maintains two subarrays in a given array:

1. The subarray that is already sorted.
2. The remaining subarray that is unsorted.


Here's a step-by-step explanation of how Selection Sort works:

1. Find the minimum element in the list.
2. Swap the minimum element in the list with the element at index 0. The minimum element is now in its final sorted position.
3. Find the minimum element in the remaining portion of the list (starting from index 1).
4. Swap this element with the element at index 1. The second-to-minimum element is now in its final sorted position.
5. Continue finding the next-minimum element in the remaining portions of the list until you have swapped all elements into their final sorted positions.