#https://www.hackerrank.com/challenges/diagonal-difference/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sum1 = 0;
    sum2 = 0;

    for i in range(len(arr)):
        sum1 += arr[i][i];
        sum2 += arr[len(arr)-1-i][i];
    res = abs(sum1-sum2);
    return res;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
