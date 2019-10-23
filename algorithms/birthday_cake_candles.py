#!/bin/python3
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# author: @engrjepmanzanillo

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.


def birthdayCakeCandles(ar):
    # get the highest candle by getting the
    # highest element in the list
    highest_candle = max(ar)
    # get the number of highest candles by
    # getting the highest candle's occurence in the list
    num_candle = 0
    for i in range(len(ar)):
        if highest_candle == ar[i]:
            num_candle += 1
    # returning number of highest candle
    return num_candle


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #ar_count = int(input())

    #ar = list(map(int, input().rstrip().split()))
    ar = [3, 2, 1, 3]

    result = birthdayCakeCandles(ar)
    print(result)

    #fptr.write(str(result) + '\n')

    # fptr.close()
