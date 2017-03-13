"""
- Worst Case:   O(n + k)
- Best Case:    O(n + k)
- Average Case: O(n + k)

Space Complexity:
- Worst Case    O(k)

Counting sort is an algorithm for sorting a collection of objects according to keys that are small integers. It operates by counting the number of objects that have each distinct key value, and using arithmetic on those counts to determine the positions of each key value in the output sequence.
"""


def countingsort(input_list):
    # Calculate the range of integer inputs
    max_input = max(input_list)
    min_input = min(input_list)
    input_range = abs(max_input - min_input + 1)

    # Calculate the histogram of key frequencies:
    count = [0 for _ in range(input_range)]
    for elt in input_list:
        count[elt + min_input] += 1

    # Calculate the starting index for each key
    total = 0
    for idx in range(input_range):
        count[idx], total = total, total + count[idx]

    # Copy to output array, preserving order of inputs with equal keys:
    result = input_list[:]
    for x in input_list:
        result[count[x - min_input]] = x - min_input
        count[x - min_input] += 1

    return result
