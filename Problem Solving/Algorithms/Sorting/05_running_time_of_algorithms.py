#https://www.hackerrank.com/challenges/runningtime/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    track = 0
    for i in range(1,len(arr)):
        num = arr[i]
        j = i-1
        while(j>=0 and arr[j]>num):
            arr[j+1] = arr[j]
            j -= 1
            track += 1
        arr[j+1] = num
    return track

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
