"""
Worst Case:   O(n log n)
Best Case:    O(n log n)
Average Case: O(n log n)
"""


def heapsort(a):
    result = a
    heapify(result, len(result))
    end = len(result) - 1
    while end > 0:
        result[end], result[0] = result[0], result[end]
        end -= 1
        siftDown(result, 0, end)
    return result


def heapify(a, count):
    start = int((count - 2) / 2)
    while start >= 0:
        siftDown(a, start, count - 1)
        start -= 1


def siftDown(a, start, end):
    root = start
    while (root * 2 + 1) <= end:
        child = root * 2 + 1
        swap = root
        if a[swap] < a[child]:
            swap = child
        if (child + 1) <= end and a[swap] < a[child + 1]:
            swap = child + 1
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            root = swap
        else:
            return
