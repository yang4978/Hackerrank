#https://www.hackerrank.com/challenges/strange-advertising/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    linked = 5//2;
    cum = linked;
    for i in range(n-1):
        linked = linked*3//2;
        cum += linked;
    return cum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
