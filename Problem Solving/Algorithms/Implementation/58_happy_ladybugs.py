#https://www.hackerrank.com/challenges/happy-ladybugs/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    c = collections.Counter(b)
    empty = c['_']
    del c['_']
    if 1 in c.values():
        return "NO"
    if(empty):
        return "YES"
    if(b[0]!=b[1] or b[-1]!=b[-2]):
        return "NO"
    for i in range(1,len(b)-1):
        if(b[i-1]!=b[i] and b[i]!=b[i+1]):
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
