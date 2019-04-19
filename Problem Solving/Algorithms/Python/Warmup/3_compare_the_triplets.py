#https://www.hackerrank.com/challenges/compare-the-triplets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    num = len(a);
    i = 0;
    c = [0,0];
    while i<num:
        if a[i] > b[i]:
            c[0] += 1;
        elif a[i] < b[i]:
            c[1] += 1;
        i += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
