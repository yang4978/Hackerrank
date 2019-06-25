#https://www.hackerrank.com/challenges/quicksort2/problem

import math
import os
import random
import re
import sys

def quickSort(arr):
    pivot = [arr[0]]
    left = []
    right = []
    for i in arr:
        if(i<arr[0]):
            left.append(i)
        if(i>arr[0]):
            right.append(i)
    if(len(left)>1):
        left = quickSort(left)
        print(*left)
    
    if(len(right)>1):
        right = quickSort(right)
        print(*right)

    return left+pivot+right

    return quickSort(left)+pivot+quickSort(right)

if __name__ ==  "__main__":
    
    n = int(input())

    arr = list(map(int,input().split()))

    print(*quickSort(arr));
