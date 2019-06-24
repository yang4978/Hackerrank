#https://www.hackerrank.com/challenges/insertionsort2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    len_arr = len(arr)
    for i in range(1,len_arr):
        num = arr[i]
        j = i-1
        while(j>=0 and arr[j]>num):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = num
        print(*arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
