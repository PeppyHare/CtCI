"""
Time complexity:
Worst Case:   O(n^2)
Best Case:    O(n)
Average Case: O(n^2)
Bubble sort, sometimes referred to as sinking sort, is a simple sorting
algorithm that repeatedly steps through the list to be sorted, compares each
pair of adjacent items and swaps them if they are in the wrong order. The pass
through the list is repeated until no swaps are needed, which indicates that the
list is sorted. The algorithm, which is a comparison sort, is named for the way
smaller or larger elements "bubble" to the top of the list. Although the
algorithm is simple, it is too slow and impractical for most problems even when
compared to insertion sort. It can be practical if the input is usually in
sorted order but may occasionally have some out-of-order elements nearly in
position.

- Wikipedia
"""


def bubblesort(a):
    swapped = True
    while swapped:
        swapped = False
        for idx in range(1, len(a)):
            if a[idx - 1] > a[idx]:
                a[idx], a[idx - 1] = a[idx - 1], a[idx]
                swapped = True
        if not swapped:
            return a
