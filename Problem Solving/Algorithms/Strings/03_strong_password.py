#https://www.hackerrank.com/challenges/strong-password/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    regex = [r'[0-9]',r'[a-z]',r'[A-Z]',r'[!@#$%^&*()\-+]']
    temp = 0
    for i in regex:
        if (re.search(i,password)):
            temp += 1;
    return max(4-temp,6-n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
