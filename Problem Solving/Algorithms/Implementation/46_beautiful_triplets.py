#https://www.hackerrank.com/challenges/beautiful-triplets/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    dic = collections.defaultdict(lambda:0)
    for i in arr:
        dic[i] += 1
    return sum([dic[i]*dic[i+d]*dic[i+2*d] for i in set(arr)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
