"""
For n keys which are integers of word size w,
Time Complexity:
- Worst Case:   O(wn)
Space Complexity:
- Worst Case:   O(w + n)
Radix sort is a non-comparative integer sorting algorithm that sorts data with
integer keys by grouping keys by the individual digits which share the same
significant position and value. As integers can represent strings of characters
and floating point numbers, radix sort is not necessarily restricted to integer
inputs.
"""


def radixsort(input_list):
    """
    In-place Least-Significant-Digit Radix Sort
    """
    radix = 10
    div = 1
    maxLength = False

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(radix)]
        for value in input_list:
            tmp = value / div
            buckets[tmp % radix].append(value)
            if maxLength and tmp > 0:
                maxLength = False

        fill_idx = 0
        for idx in range(radix):
            bucket = buckets[idx]
            for value in bucket:
                input_list[fill_idx] = value
                fill_idx += 1

        # Move on to the next digit
        div = div * 10
    return input_list
