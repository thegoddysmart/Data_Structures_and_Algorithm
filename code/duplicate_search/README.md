# Duplicate Count

In this exercise you will count the number of duplicates for a given value in a sorted list using binary search.

## Starter Code

To begin, you are given `search.py`. This file contains a `duplicate_count_linear()` function, which uses a linear searching strategy to count the number of duplicates of a given number in a sorted list.

## Your Task

Your task is to implement the `duplicate_count_binary()` function, which should use binary search to count the number of duplicate values of whatever `num` is passed in as a parameter.

Some notes:

- `duplicate_count_binary()` may assume that the given `lst` is in sorted order.
- You only need to use binary search to find one of the duplicates of the given `num`. Once found, you can use a linear search to look left and right in the list for how many duplicates (if any) there are.
- The function should return the number of *duplicates*, so if `num` only appears once, then the number of duplicates is 0.
- If the number does not appear at all in the list, the function should still return 0.

Recall the basic binary search algorithm:

1. Look at the middle element of the list. If it's the value you're looking for, you don't need to search further. Otherwise, if it's less than the element you're looking for, you can continue searching in the right half of the list. Otherwise, if it's greater than the element you're looking for, you can continue searching in teh left half of the list.
2. Repeat the above "cut in half" strategy until you either find the value you're searching for, or can be sure that the value does not exist in the list.

It may also help to review the binary search code presented in the videos from this week.

## Test Cases

In `test_search.py`, there are some unit tests that test the functionality of `duplicate_count_linear()`. Note: even though this function doesn't require the input list to be sorted, the tests all have sorted lists.

Add unit tests to `test_search.py` to validate the functionality of `duplicate_count_binary()` as well.