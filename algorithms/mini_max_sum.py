#!/bin/python3
# https://www.hackerrank.com/challenges/mini-max-sum/problem
# author: @engrjepmanzanillo

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    # will use bubble sorting algorithm to arrange
    # elements from lowest to highest
    # this is to assure that elements are sorted for getting
    # minimum and maximum sum
    i = 0
    while i < len(arr):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        i += 1
    # getting minimum sum by slicing the highest element
    min_sum = sum(arr[:len(arr)-1])
    # getting maximum sum by slicing the lowest element
    max_sum = sum(arr[1:])

    print(f'{min_sum} {max_sum}')


if __name__ == '__main__':
    #arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
