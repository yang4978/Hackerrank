#https://www.hackerrank.com/challenges/kaprekar-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    result = []
    for x in range(p,q+1):
        mod = 10**((1+len(str(x*x)))//2)
        if(x*x%mod+x*x//mod==x):
            result.append(x)
    if(result):
        print(*result)
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
