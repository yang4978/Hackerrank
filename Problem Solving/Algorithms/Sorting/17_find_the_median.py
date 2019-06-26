#https://www.hackerrank.com/challenges/find-the-median/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def quicksort(arr):
    if(len(arr)<2):
        return arr
    baseValue = arr[0]
    left = []
    equal = []
    right = []
    for i in arr:
        if(i<baseValue):
            left.append(i)
        elif(i==baseValue):
            equal.append(i)
        else:
            right.append(i)
    return quicksort(left)+equal+quicksort(right)


def findMedian(arr):
    arr = quicksort(arr)
    return arr[len(arr)//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
