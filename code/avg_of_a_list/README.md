# List Average

`listavg.py` contains the definition of a `ListAverage` class. This class has an instance variable that contains a list of numbers, as well as an `add()` method to add more numbers to the list. It also has a method `compute_avg()` that computes and returns the average value of the list.

However, the implementation of `compute_avg()` is an inefficient way of computing the average.

## Your Task

Implement the `compute_avg_faster()` method so that it computes the average of the list *without* iterating over the list. You may *not* use the Python `sum()` function as a part of your implementation. However, you will need to add at least one other instance variable to the class, and will also need to modify one of the existing methods.

## Test Cases

In `test_listavg.py`, add unit tests that test the functionality of your `ListAverage`.