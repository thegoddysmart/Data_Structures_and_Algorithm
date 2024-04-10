# Insertion Sort Analysis

In this exercise we will experimentally derive the running time of insertion sort. In other words, instead of finding the running time by analyzing the loops of the algorithm, we will count the number of comparisons and moves the algorithm makes and use those measurements to derive the big-O running time.

We will conduct our analysis for both the worst case (random lists) and best case (almost sorted lists) behavior.

## Starter Code

You are given the file `sort.py`, which includes the implementation of insertion sort. It is in a Python class called `Sort`, which has two fields: `comps` and `moves`. These variables track the number of comparisons and moves made by the sorting algorithm, respectively. On creating an instance of the `Sort` class, `comps` and `moves` are initialized to zero.

The `insertion_sort()` method uses the `compare()` method to compare two elements of a list while incrementing the `comps` field. For example, instead of:

```python
if to_insert < lst[j - 1]:
```

The method instead uses:

```python
if self.compare(to_insert < lst[j - 1]):
```

This method returns the result of the comparison (either `True` or `False`), and increments the count of comparisons that the class maintains.

Similarly, the `move()` method moves a value into a given index of the list, and increments the count of moves performed by the algorithm overall.

You are also given:

- A `random_list()` function that generates a random integer list of length `n`.
- An `almost_sorted_list()` function that generates an integer list of length `n` that is almost sorted. *You do not need to understand how this function works.*
- Code in the main part of the script that generates random and almost sorted lists, sorts them, and reports the number of comparisons and moves for each.

## Steps to Complete

1. Modify the code in `sort.py` to test how many comparisons and moves `insertion_sort()` makes on *random* lists of various lengths. You should run the algorithm on lists of at least three different sizes (e.g., 1000, 2000, and 4000). Record the number of comparisons and moves for each trial below.

Be sure to do the following before each call to the `insertion_sort()` function:
      - Generate a new list. You don't want to pass the list you just sorted back to the algorithm.
      - Call the `reset_stats()` method of the `Sort` object to reset the comparisons and moves to zero. If you don't, the number of comparisons and moves will continue to increment for each invocation of the algorithm.

Below is the table of results from running insertion sort on random lists of various sizes:

| List Size | Number of Comps | Number of Moves |
|-----------|-----------------|-----------------|
|           |                 |                 |
|           |                 |                 |
|           |                 |                 |

2. Modify the code in `sort.py` to test how many comparisons and moves `insertion_sort()` makes on *almost sorted* lists of various sizes. The same guidelines as (1) apply here. Record the number of comparisons and moves for each trial below.

Below is the table of results from running insertion sort on almost sorted lists of various sizes:

| List Size | Number of Comps | Number of Moves |
|-----------|-----------------|-----------------|
|           |                 |                 |
|           |                 |                 |
|           |                 |                 |

3. Using the experimental data, calculate the big-O time complexity for `insertion_sort()`. For both types of input (random lists and almost sorted lists), show the time complexity for moves, the time complexity for comparisons, and the overall time complexity.

    - To do so, observe what happens to the number of comparisons when the size of the list doubles for random lists. Does the number of comparisons double? Quadruple? Increase by a factor of `nlogn`? Use this to determine the big-O for comparisons.
    - Repeat the above process to find the big-O expression for the number of moves for random lists.
    - Combine the two big-O expressions to find the total big-O expression for random lists.

Then, repeat this analysis for almost sorted lists.