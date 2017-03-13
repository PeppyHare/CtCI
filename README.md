# CtCI
[![Build Status](https://travis-ci.org/PeppyHare/CtCI.svg?branch=master)](https://travis-ci.org/PeppyHare/CtCI)

I know everyone and their grandmother is trying to plow through [Cracking the Code Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850) to ace their technical interviews, but it really is a tremendously helpful study guide. This repo just contains my worked solutions to a number of the problems/suggested exercises in that book (and others) in Python. None of this is by any means meant to hold up to production code standards, but neither are these solutions as unpolished as technical interview code might be.

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

### [Radix Sort](sorting/radixsort.py)
Time Complexity
- Worst Case:   O(nw)
- Best Case:    O(nw)
- Average Case: O(nw)

### [Bucket Sort (Bin Sort)](sorting/bucketsort.py)
Time Complexity
- Worst Case:   O(n^2)
- Best Case:    O(n + k)
- Average Case: O(n + k)

Space Complexity:
- Worst Case:   O(nk)

where w is the length of the longest number and n is the size of the input array. Note: if k is greater than log(n), then a different sorting algorithm would be faster, but in reality we can always change the radix such that `k < log(n)`

## Constructive Algorithm Exercises

### [Matrix flipping problem](algorithms/matrixflipper.py)
Taken from [this problem on HackerRank](https://www.hackerrank.com/challenges/flipping-the-matrix)

_Sean invented a game involving a 2n x 2n matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times, and the goal of the game is to maximize the sum of the elements in the n x n submatrix located in the upper-left corner of the 2n x 2n matrix (i.e. its upper-left quadrant)._

## Dynamic Programming Exercises

### [Change Counting Problem](algorithms/coincounter.py)
Taken from [this problem on HackerRank](https://www.hackerrank.com/challenges/coin-change)

_How many different ways can you make change for an amount, given a list of coins? In this problem, your code will need to efficiently compute the answer._


# Running Tests

```shell
python -m unittest discover tests
```