"""
Worst Case:   O(n^2)
Best Case:    O(n^2)
Average Case: O(n^2)
The algorithm divides the input list into two parts: the sublist of items
already sorted, which is built up from left to right at the front (left) of the
list, and the sublist of items remaining to be sorted that occupy the rest of
the list. Initially, the sorted sublist is empty and the unsorted sublist is the
entire input list. The algorithm proceeds by finding the smallest (or largest,
depending on sorting order) element in the unsorted sublist, exchanging
(swapping) it with the leftmost unsorted element (putting it in sorted order),
and moving the sublist boundaries one element to the right.
"""


def selectionsort(a):
    for jj in range(len(a)):
        imin = jj
        for ii in range(imin, len(a)):
            if a[ii] < a[imin]:
                imin = ii
        if imin != jj:
            a[imin], a[jj] = a[jj], a[imin]
    return a
