#https://www.hackerrank.com/challenges/larrys-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A):
    return "NO" if(sum([sum([1 if A[i]>A[num] else 0 for i in range(num)]) for num in range(len(A))])%2) else "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
