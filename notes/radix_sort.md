# Radix sort

Both of the sorts we've considered so far are comparative sorting algorithms. They sort the lists by comparing elements of the list against each other to find their relative orderings, and puts them into position based on that ordering.

But that's not the only approach to sorting! One alternative is distributive sorting, which distributes the values of the list into positions based on an inherent characteristics of the values themselves.

In summary, the algorithm is as follows:

1. Place the values of the list into buckets 0-9 according to their least significant digit (the "ones" digit). At this point, the values are sorted with respect to their ones digits only.

2. Iterate over the values in the buckets, starting from the 0 bucket and proceeding all the way to the 9 bucket. Place the values of the list into buckets 0-9 according to their next significant digit (the "tens" digit). At this point, the values are sorted with respect to both their tens and ones digits.

3. Continue iterating over the values in the buckets (from 0 to 9), consider the next significant digit for each pass. Stop when there are no more digits to consider.

4. Format the buckets back into a list and return the list.