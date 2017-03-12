# CtCI

I know everyone and their grandmother is trying to plow through [Cracking the Code Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850) to ace their technical interviews, but it really is a tremendously helpful study guide. This repo just contains my worked solutions to a number of the problems in that book (and others) in Python. None of this is by any means meant to hold up to production code standards, but neither are these solutions as unpolished as technical interview code might be.

## Sorting Algorithms

### [Heapsort](sorting/heapsort.py)
Time Complexity
- Worst Case:   O(n log n)
- Best Case:    O(n log n)
- Average Case: O(n log n)


### [Bubble Sort](sorting/bubblesort.py)
Time Complexity
- Worst Case:   O(n^2)
- Best Case:    O(n)
- Average Case: O(n^2)

### [Insertion Sort](sorting/insertionsort.py)
Time Complexity
- Worst Case:   O(n^2)
- Best Case:    O(n)
- Average Case: O(n^2)

### [Mergesort](sorting/mergesort.py)
Time Complexity
- Worst Case:   O(n log n)
- Best Case:    O(n log n)
- Average Case: O(n log n)

Space Complexity:
- Worst Case:   O(n)

### [Quicksort](sorting/quicksort.py)
Time Complexity
- Worst Case:   O(n^2)
- Best Case:    O(n log n)
- Average Case: O(n log n)

### [Selection Sort](sorting/selectionsort.py)
Time Complexity
- Worst Case:   O(n^2)
- Best Case:    O(n^2)
- Average Case: O(n^2)

## Dynamic Programming Exercises

### [Change Counting Problem](dynamicprogramming/coincounter.py)
Taken from [this problem on HackerRank](https://www.hackerrank.com/challenges/coin-change)

_How many different ways can you make change for an amount, given a list of coins? In this problem, your code will need to efficiently compute the answer._


# Running Tests

```shell
python -m unittest discover tests
```