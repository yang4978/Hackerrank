#https://www.hackerrank.com/challenges/almost-sorted/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    arr_sor = sorted(arr)
    num = []
    for i in range(len(arr)):
        if(arr[i]!= arr_sor[i]):
            num.append(i)

    if(len(num)==2):
        print("yes\nswap",num[0]+1,num[-1]+1)
    elif(arr[:num[0]]+arr[num[-1]:num[0]-1:-1]+arr[num[-1]+1:]==arr_sor):
        print("yes\nreverse",num[0]+1,num[-1]+1)
    else:
        print("no")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
