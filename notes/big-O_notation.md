# Big-O Notation

Big-O notation is a mathematical notation used to describe the limiting behavior of a function when the argument tends towards a particular value or infinity. In computer science, it is primarily used to analyze the time complexity or space complexity of algorithms.

Simply speaking, imagine you have a list of numbers, and you want to find a particular number in that list. Big-O notation helps us understand how many steps it will take to find that number, depending on how big the list is.


## Common Classes:

- **O(1) - Constant Time**: Runtime remains constant regardless of the input size. It's like doing something super quick, no matter how big the list is. Imagine you have a magic trick that always works instantly, no matter how many people are watching!

- **O(log n) - Logarithmic Time**: Runtime grows logarithmically with the input size.This one is like when you have a big phone book, and you want to find someone's number. You start in the middle and keep splitting the book in half until you find the right page. It's pretty fast!

- **O(n) - Linear Time**: Runtime grows linearly with the input size. Imagine you have a bunch of books, and you need to find one with a specific title. You have to look through each book one by one until you find the right one. This takes longer as you have more books.

- **O(n log n) - Linearithmic Time**: Runtime grows linearithmically with the input size. This is a bit like sorting a deck of cards. You have to compare and arrange each card, but it's not as fast as just looking for one card.

- **O(n^2) - Quadratic Time**: Runtime grows quadratically with the input size. Imagine you're trying to make a square garden by planting seeds in rows and columns. The more seeds you plant, the longer it takes to finish your garden.

- **O(2^n) - Exponential Time**: Runtime grows exponentially with the input size. This one grows really fast! It's like when you have a puzzle, and every time you add a piece, it takes twice as long to solve.

- **O(n!) - Factorial Time**: Runtime grows factorially with the input size. This is like the slowest one! It's like when you have to try every possible arrangement to solve a problem. It takes forever, especially as the number of possibilities grows.


**The following are sorted from slowest to fastest**

- `O(n!)` ("factorial time")
- O(c<sup>n</sup>) where `c` is some constant ("exponential time")
- O(n<sup>c</sup>) where `c` is some constant >2 ("polynomial time")
- O(n<sup>2</sup>) ("quadratic time")
- `O(nlogn)` ("linearithmic time" or "log-linear time")
- `O(n)` ("linear time")
- `O(logn)` ("logarithmic time")
- `O(1)` ("constant time")


## Rules of Big-O Notation

1. Worst-case Analysis: Big-O notation typically represents the worst-case scenario of an algorithm's performance. It describes the upper limit on the algorithm's execution time or memory usage, ensuring that the algorithm performs no worse than the specified complexity class for any input.

2. Asymptotic Analysis: Big-O notation focuses on the behavior of an algorithm as the input size approaches infinity. It ignores constant factors and lower-order terms, capturing the long-term growth rate of the algorithm's performance.

3. Dominant Term: In Big-O notation, only the dominant term or the term with the highest growth rate is considered. For example, in O(n^2 + n), the dominant term is n^2, so the complexity is expressed as O(n^2).

4. Multiplicative Constants: Big-O notation disregards multiplicative constants when analyzing algorithm complexity. For example, O(2n) and O(n) are considered equivalent because both represent linear growth.

5. Additive Constants and Lower-order Terms: Big-O notation ignores additive constants and lower-order terms. For example, O(n^2 + n) simplifies to O(n^2), and O(n^3 + n^2) simplifies to O(n^3).


## Heuristics for Finding Big-O Expressions

1. **Loops up to n**:
    One of the simplest cases for analyzing time complexity is when an algorithm contains a loop that iterates based on the size of the input (denoted as n). For example, a loop that iterates over a list of length n has a time complexity of O(n). Even if the loop iterates a fraction of n times, for sufficiently large values of n, the fraction becomes negligible.

    ```python
    def print_list(lst):
        n = len(lst)
        for i in range(n):
        print(lst[i])
    ```

2. **Loops up to a constant value**:
    Some loops have a fixed number of iterations regardless of the input size. For instance, a loop that iterates three times irrespective of the input size has a constant time complexity, denoted as O(1).

    ```python
    def print_first_three(lst):
        for i in range(3):
        print(lst[i])
    ```

3. **Back-to-back loops**:
    When an algorithm contains consecutive loops, the time complexities of these loops add up. For example, if two loops both iterate over a list of size n, the overall time complexity is O(n) + O(n) = O(2 * n) = O(n).

4. **Nested loops**:
    Nested loops result in a multiplication of their time complexities. For instance, if an outer loop iterates n times and an inner loop within it also iterates n times, the overall time complexity becomes O(n) * O(n) = O(n^2).

5. **Loops containing functions**:
    If loops call functions within them, consider the time complexity of those functions as well. Nested functions can compound the overall time complexity of the algorithm.

6. **Loops on different inputs**:
    When an algorithm operates on multiple inputs of potentially different sizes, use different symbols (such as n and m) to represent their lengths. The overall time complexity is then expressed as O(n + m), accounting for the sizes of both inputs.
