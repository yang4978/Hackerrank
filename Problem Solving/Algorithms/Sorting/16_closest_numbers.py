#https://www.hackerrank.com/challenges/closest-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    result = []
    min_dist = 2*10**7
    for i in range(len(arr)-1):
        if(abs(arr[i+1]-arr[i])<min_dist):
            min_dist = abs(arr[i+1]-arr[i])
            result = [arr[i],arr[i+1]]
        elif(abs(arr[i+1]-arr[i])==min_dist):
            result += [arr[i],arr[i+1]]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
