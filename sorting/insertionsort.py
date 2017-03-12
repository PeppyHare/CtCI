"""
Worst Case:   O(n^2)
Best Case:    O(n)
Average Case: O(n^2)
"""


def insertionsort(a):
    for ii in range(len(a)):
        jj = ii
        while jj > 0 and a[jj - 1] > a[jj]:
            a[jj], a[jj - 1] = a[jj - 1], a[jj]
            jj -= 1
    return a
