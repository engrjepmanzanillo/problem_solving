#!/bin/python3
# https://www.hackerrank.com/challenges/time-conversion/problem
# author: @engrjepmanzanillo

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    #
    # Write your code here.
    #
    # will use string manipulation
    hour = s[:2]
    minute = s[3:5]
    seconds = s[6:8]
    if s[-2:] == 'AM' and hour == '12':
        return f'00:{minute}:{seconds}'
    elif s[-2:] == 'AM' and int(hour) < 12:
        return s[:-2]
    elif s[-2:] == 'PM' and hour == '12':
        return s[:-2]
    else:
        return f'{int(hour)+12}:{minute}:{seconds}'


if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = '11:05:45AM'

    result = timeConversion(s1)
    print(result)
    # f.write(result + '\n')

    # f.close()
