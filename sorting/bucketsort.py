"""
- Worst Case:   O(n^2)
- Best Case:    O(n + k)
- Average Case: O(n + k)

where n is the number of elements in the array to be sorted, and k is the number
of buckets

Bucket sort is a sorting algorithm that works by distributing the elements of an
array into a number of buckets. Each bucket is then sorted individually, either
using a different sorting algorithm or by recursively applying the bucket
sorting algorithm.

This implementation will work only on a list of integers
"""

from quicksort import quicksort


def bucketsort(input_list):
    biggest = max(input_list)
    print("\nbiggest: %f" % biggest)
    n_buckets = biggest / 10 + 1
    print("\nn_buckets: %d" % n_buckets)
    buckets = [list() for _ in range(n_buckets)]
    for idx, x in enumerate(input_list):
        buckets[x / 10].append(x)
    print("\nbuckets:", buckets)
    for idx, bucket in enumerate(buckets):
        buckets[idx] = quicksort(bucket)
    print("\nbuckets:", buckets)
    result = []
    for bucket in buckets:
        result += bucket
    return result
