#https://www.hackerrank.com/challenges/insertion-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort(arr):
    n = len(arr)
    if n==1:
        return 0
    n1 = n//2
    n2 = n - n1
    left = arr[:n1]
    right = arr[n1:]
    ans= insertionSort(left)+insertionSort(right)

    l = 0
    r = 0

    for i in range(n):
        if(l<n1 and r<n2):
            if(left[l]<=right[r]):
                arr[i] = left[l]
                l += 1
            else:
                arr[i]=right[r]
                r += 1
                ans += n1-l
        elif(l<n1):
            arr[i] = left[l]
            l += 1
        else:
            arr[i] = right[r]
            r += 1

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
