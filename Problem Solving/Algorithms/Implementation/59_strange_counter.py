#https://www.hackerrank.com/challenges/strange-code/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    series = 1
    while(t>series*3):
        t -= series*3
        series *= 2
    return 3*series+1-t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
