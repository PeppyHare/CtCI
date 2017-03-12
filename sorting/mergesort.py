"""
Merge sort:

- Divide the unsorted list "a" into n sublists, each containing 1 element
- Repeatedly merge sublists to produce new sorted sublists until there is only 1
  sublist remaining. This list is sorted
"""


def mergesort(a):
    if len(a) <= 1:
        return a

    left = a[:len(a) / 2]
    right = a[len(a) / 2:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    if left:
        result.extend(left)
    if right:
        result.extend(right)

    return result
