#https://www.hackerrank.com/challenges/minimum-distances/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the minimumDistances function below.
def minimumDistances(a):
    dic = collections.defaultdict(lambda:[])
    for i in range(0,len(a)):
        if(a.count(a[i])>=2):
            dic[a[i]].append(i)
    if(dic.values()):
        return min([min([v[i]-v[i-1] for i in range(1,len(v))]) for v in dic.values()])
    else:
        return -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
