#https://www.hackerrank.com/challenges/birthday-cake-candles/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    num_max = 0;
    max_ar = max(ar);
    for i in ar:
        if i == max_ar:
            num_max += 1;
    return num_max;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
