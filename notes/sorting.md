 # Sorting
 
 **Sorting** refers to the process of rearranging elements in a collection (such as an array or a list) in a specific order, typically ascending or descending based on some criteria.

## Stability
A sorting algorithm is stable if it preserves the relative order of equal elements in the sorted output. In other words, if two elements have the same key value, the one that appears first in the original input array should appear first in the sorted output.

## In-place Sorting
An in-place sorting algorithm sorts the elements within the input array itself without requiring any additional memory space proportional to the input size. In-place sorting algorithms are memory-efficient but may sacrifice some performance.


## Comparison-based Sorting
Most sorting algorithms are comparison-based, meaning they compare elements pairwise and swap them based on the comparison result. These algorithms typically have a time complexity of at least O(n log n), where n is the number of elements to be sorted.

## Non-comparison Sorting
Some sorting algorithms, such as Counting Sort and Radix Sort, do not rely on element comparisons to achieve sorting. These algorithms can achieve linear time complexity under certain conditions but may have limitations on the types of data they can sort.

## Time Complexity
The time complexity of a sorting algorithm describes how its runtime grows with the size of the input data. It provides an upper bound on the number of basic operations (such as comparisons and swaps) performed by the algorithm.

## Space Complexity
The space complexity of a sorting algorithm describes the amount of additional memory space (apart from the input array) required by the algorithm to perform sorting. It includes variables, arrays, and other data structures used during the sorting process.



# Comparison-based Sorting

Comparison-based sorting algorithms are algorithms that sort a collection of elements by comparing pairs of elements and rearranging them based on the comparison result.

Here are some key characteristics of comparison-based sorting algorithms:

1. **Comparisons**: The primary operation in comparison-based sorting algorithms is the comparison of elements. Algorithms compare elements pairwise using some comparison operator (e.g., less than, greater than, or equal to) and determine their relative order.

2. **Swapping**: After comparing elements, sorting algorithms may need to swap elements to rearrange them according to the desired order. Swapping is typically done to move smaller elements towards the beginning of the collection and larger elements towards the end.

3. **Time Complexity**: The time complexity of comparison-based sorting algorithms is typically expressed in terms of the number of comparisons and swaps performed. The most efficient comparison-based sorting algorithms, such as Merge Sort and Quick Sort, achieve a time complexity of `O(n log n)` in the average and best cases.

4. **Space Complexity**: Comparison-based sorting algorithms may require additional memory space for temporary variables, recursion stacks (in recursive algorithms), or auxiliary data structures. However, the space complexity of these algorithms is usually O(1) or O(log n) additional space apart from the input array.

5. **Stability**: Some comparison-based sorting algorithms, such as Merge Sort and Insertion Sort, are stable, meaning they preserve the relative order of equal elements in the sorted output. Stability can be important in applications where the original order of equal elements needs to be maintained.

6. **Adaptability**: Some comparison-based sorting algorithms, such as Insertion Sort and Bubble Sort, can be adaptive, meaning they may perform better on partially sorted or nearly sorted input arrays compared to completely unsorted arrays.

 Comparisons and moves are fundamental operations in sorting algorithms, and analyzing the number of comparisons and moves can provide insights into the efficiency of an algorithm.

 In many comparison-based sorting algorithms, the number of comparisons is often the dominating factor in determining the overall time complexity. This is because comparisons are typically more time-consuming operations compared to simple moves or swaps. Therefore, when analyzing the efficiency of a sorting algorithm, it's common to focus on the number of comparisons made.

 However, moves or swaps also contribute to the overall runtime of a sorting algorithm, especially when dealing with large datasets or when the cost of moving elements is significant (e.g., moving large objects in memory). Therefore, both comparisons and moves are important factors to consider when evaluating the performance of a sorting algorithm.

**Examples of popular comparison-based sorting algorithms include**:

- **Bubble Sort**: A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

- **Selection Sort**: A simple sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion of the list and moves it to the sorted portion.

- **Insertion Sort**: A simple sorting algorithm that builds the sorted list one element at a time by repeatedly inserting the next unsorted element into its correct position in the sorted portion.

- **Merge Sort**: A divide-and-conquer sorting algorithm that recursively divides the input array into smaller subarrays, sorts them independently, and then merges the sorted subarrays to produce the final sorted output.

- **Quick Sort**: A divide-and-conquer sorting algorithm that partitions the input array into two subarrays based on a pivot element, recursively sorts the subarrays, and then combines them to form the sorted output.