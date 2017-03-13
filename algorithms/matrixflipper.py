"""
Sean invented a game involving a 2n x 2n matrix where each cell of the matrix
contains an integer. He can reverse any of its rows or columns any number of
times, and the goal of the game is to maximize the sum of the elements in the n
x n submatrix located in the upper-left corner of the 2n x 2n matrix (i.e. its
upper-left quadrant).

Input format
 - n: The size of the input matrix will be 2n x 2n
 - input_matrix: a 2n x 2n matrix of integers.

Output format:
- matrixflipper(n, A) gives the maximum possible sum of the elements in the
  matrix's upper-left quadrant.
"""


def matrixflipper(n, A):
    maxsum = 0
    N = 2 * n
    for ii in range(n):
        for jj in range(n):
            # Find the maximal element which can be moved to A[ii, jj]
            r_1 = ii
            c_1 = jj
            r_2 = N - ii - 1
            c_2 = N - jj - 1
            maxsum += max([A[r_1][c_1], A[r_1][c_2], A[r_2][c_1], A[r_2][c_2]])
    return maxsum
