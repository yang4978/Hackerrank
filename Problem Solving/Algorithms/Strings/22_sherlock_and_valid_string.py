#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    num = [s.count(i) for i in set(s)]
    return 'YES' if((num.count(min(num))>=len(num)-1 and max(num)-min(num)<=1) or (num.count(max(num))==len(num)-1 and min(num)==1)) else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
