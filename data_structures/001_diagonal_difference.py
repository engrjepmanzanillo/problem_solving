# https://www.hackerrank.com/challenges/diagonal-difference/problem
# engrjepmanzanillo

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    left_to_right = []
    right_to_left = []
    k = len(arr)
    for i in range(k):
        left_to_right.append(arr[i][i])

    for i in range(k):
        right_to_left.append(arr[i][k-i-1])
    return abs(sum(left_to_right) - sum(right_to_left))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    arr = [[11, 2, 4],
           [4, 5, 6],
           [10, 8, -12]]

# for _ in range(n):
#    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)
# fptr.write(str(result) + '\n')

# fptr.close()
