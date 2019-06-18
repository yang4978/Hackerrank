#https://www.hackerrank.com/challenges/alternating-characters/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    temp = s
    while(re.search(r'([a-zA-Z])\1+',temp)):
        temp = re.sub(r'([a-zA-Z])\1+','+',temp)
    return len(s) - len(temp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
