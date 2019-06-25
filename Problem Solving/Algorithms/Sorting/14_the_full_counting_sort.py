#https://www.hackerrank.com/challenges/countingsort4/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    for i in range(len(arr)//2):
        arr[i][1] = '-'
    count = [0]*100
    for i in arr:
        count[int(i[0])] += 1;
    
    for i in range(1,100):
        count[i] += count[i-1]

    result = ['-'] * len(arr)
    
    for i in range(len(arr)-1,-1,-1):
        result[count[int(arr[i][0])]-1] = arr[i][1]
        count[int(arr[i][0])] -= 1
    
    print((" ").join(result))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
