#https://www.hackerrank.com/challenges/quicksort4/problem

import sys

import math
import os
import random
import re
import sys

swap = 0;
shift = 0;

def insertion_sort(arr):
    global shift
    for i in range(1,len(arr)):
        temp = arr[i]
        j=i-1
        while(j>=0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j -= 1
            shift += 1
        arr[j+1] = temp

def getPartitionIdx(arr,start,end):
    idx = start
    global swap
    for i in range(start,end):
        if(arr[i]<=arr[end]):  
            swap += 1
            arr[i],arr[idx] = arr[idx],arr[i]
            idx += 1
    arr[idx],arr[end] = arr[end],arr[idx]
    swap += 1
    return idx    

def inplaceQuickSort(arr,start,end):
    if(start<end):
        idx = getPartitionIdx(arr,start,end)
        inplaceQuickSort(arr,start,idx-1)
        inplaceQuickSort(arr,idx+1,end)


if __name__ ==  "__main__":

    n = int(input())

    arr_insert = list(map(int,input().split()))
    arr_quick = arr_insert[:]

    insertion_sort(arr_insert)
    inplaceQuickSort(arr_quick,0,n-1)

    print(shift-swap)

