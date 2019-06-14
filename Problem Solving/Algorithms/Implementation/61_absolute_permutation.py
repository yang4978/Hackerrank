#https://www.hackerrank.com/challenges/absolute-permutation/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if(k==0):
        return [i+1 for i in range(n)]
    elif(n%(2*k)):
        return [-1]
    else:
        result = [0]*n
        for i in range(n//k//2):
            for j in range(k):
                result[j+i*2*k]=i*2*k+k+j+1
                result[k+j+i*2*k]=i*2*k+j+1
        return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
