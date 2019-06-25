#https://www.hackerrank.com/challenges/quicksort3/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

import math
import os
import random
import re
import sys

def getPartitionIdx(A, lo, hi):
    i=lo-1
    pivot = A[hi]
    for j in range(lo, hi):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[hi] = A[hi], A[i+1]
    print (*A)
    return (i+1)

def inplaceQuickSort(A, lo, hi):
    if(lo < hi):
        p=getPartitionIdx(A, lo, hi)
        inplaceQuickSort(A, lo, p-1)
        inplaceQuickSort(A, p+1, hi)

if __name__ ==  "__main__":

    n = int(input())

    arr = list(map(int,input().split()))

    inplaceQuickSort(arr,0,n-1)
