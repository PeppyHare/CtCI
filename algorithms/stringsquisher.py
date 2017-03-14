"""
Problem Statement:

String compression: implement a method to perform basic string compression using counts of characters.

"aabcccccaaa" -> "a2b1c5a3"

If compressed string not smaller than original, return the original string

Assume input only contains [a-z]
"""


def output_string_length(s):
    nsequences = 0
    prev_char = ""
    for char in s:
        if prev_char != char:
            nsequences += 1
            prev_char = char
    return nsequences * 2


def stringsquisher(s):
    if output_string_length(s) >= len(s):
        return s
    current_idx = -2
    last_char = ""
    output = []
    for char in s:
        if char == last_char:
            # same as last char
            output[current_idx + 1] = output[current_idx + 1] + 1
        else:
            # diff from last char
            output.append(char)
            output.append(1)
            current_idx += 2
            last_char = char
    output = map(str, output)
    return "".join(output)
