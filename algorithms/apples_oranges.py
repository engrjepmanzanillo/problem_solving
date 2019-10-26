#!/bin/python3
# author @jepmanzanillo

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_loc = [(x + a) >= s and (x + a) <= t for x in apples]
    oranges_loc = [(x + b) >= s and (x + b) <= t for x in oranges]
    apple_count = apples_loc.count(True)
    orange_count = oranges_loc.count(True)
    print(apple_count)
    print(orange_count)


if __name__ == '__main__':
    #st = input().split()

    s = 7

    t = 11

    #ab = input().split()

    a = 5

    b = 15

    #mn = input().split()

    m = 3

    n = 2

    #apples = list(map(int, input().rstrip().split()))
    apples = [-2, 2, 1]

    #oranges = list(map(int, input().rstrip().split()))
    oranges = [5, -6]

    countApplesAndOranges(s, t, a, b, apples, oranges)
