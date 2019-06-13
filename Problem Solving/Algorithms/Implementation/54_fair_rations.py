#https://www.hackerrank.com/challenges/fair-rations/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    even = [i for i in range(len(B)) if B[i]%2]

    if(len(even)%2):
        return "NO"
    else:
        return 2*sum([even[i]-even[i-1] for i in range(1,len(even),2)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
