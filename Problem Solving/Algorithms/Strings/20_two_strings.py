#https://www.hackerrank.com/challenges/two-strings/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    return 'YES' if sum((Counter(s1)&Counter(s2)).values()) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
