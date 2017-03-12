"""
Worst Case:   O(n^2)
Best Case:    O(n)
Average Case: O(n^2)
Insertion sort
iterates, consuming one input element each repetition, and growing a sorted
output list. Each iteration, insertion sort removes one element from the input
data, finds the location it belongs within the sorted list, and inserts it
there. It repeats until no input elements remain.
"""


def insertionsort(a):
    for ii in range(len(a)):
        jj = ii
        while jj > 0 and a[jj - 1] > a[jj]:
            a[jj], a[jj - 1] = a[jj - 1], a[jj]
            jj -= 1
    return a
