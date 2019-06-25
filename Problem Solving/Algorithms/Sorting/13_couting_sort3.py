#https://www.hackerrank.com/challenges/countingsort3/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    count = [0]*100
    for i in arr:
        count[i] += 1
    for i in range(1,100):
        count[i] += count[i-1]
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = []

    for _ in range(n):
        temp_num,temp_string = input().split()
        arr.append(int(temp_num))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


