#https://www.hackerrank.com/challenges/3d-surface-area/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    result = 0
    n_H = len(A)
    n_W = len(A[0])
    for i in range(n_H):
        for j in range(n_W):
            result += 2+4*A[i][j]
            if(j<n_W-1):
                result -= 2*min(A[i][j],A[i][j+1])
            if(i<n_H-1):
                result -= 2*min(A[i][j],A[i+1][j])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
