"""
Code Documentation: Timing Execution of Functions with timeit

This Python script demonstrates how to use the timeit library to measure the execution time of functions.
It compares the execution time of two functions: factorial calculation and insertion sort.

Author: Godfred Awudi
Date: 4th April, 2024

Dependencies:
    - Python 3.x

Usage:
    Run the script using a Python interpreter. The execution times of the factorial function and insertion sort function
    will be printed to the console.

Example:
    $ python timing_functions.py
"""

import timeit

def factorial(n):
    """
    Compute the factorial of a given non-negative integer.

    Parameters:
        n (int): The integer for which to compute the factorial.

    Returns:
        int: The factorial of the input integer n.
    """
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def insertion_sort(a_list):
    """
    Sort a list of elements using the insertion sort algorithm.

    Parameters:
        a_list (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    results = [a_list[0]]

    for item in a_list:
        if item >= results[-1]:
            results.append(item)
            continue

        for i in range(len(results)):
            if item <= results[i]:
                results.insert(i, item)
                break

    return results

if __name__ == "__main__":
    # Create Timer objects for both functions
    factorial_timer = timeit.Timer(stmt=lambda: factorial(5))
    insertion_sort_timer = timeit.Timer(stmt=lambda: insertion_sort([5, 4, 3, 2, 1]))

    # Run the timers and print the execution times
    print("Factorial function execution time:", factorial_timer.timeit(number=1000))
    print("Insertion sort function execution time:", insertion_sort_timer.timeit(number=1000))
