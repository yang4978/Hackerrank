#https://www.hackerrank.com/challenges/quicksort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    left = []
    equal = []
    right = []
    for i in arr:
        if(i==arr[0]):
            equal.append(i)
        elif(i>arr[0]):
            right.append(i)
        else:
            left.append(i)
    return left+equal+right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
