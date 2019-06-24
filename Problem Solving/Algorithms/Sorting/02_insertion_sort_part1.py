#https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    num = arr[-1]
    i = len(arr)-2
    while(i>-1):
        arr[i+1] = arr[i]
        if(arr[i]<num):
            arr[i+1] = num
            print(*arr)
            return
        print(*arr)
        i-=1
    if(i==-1):
        arr[0] = num
        print(*arr)
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
