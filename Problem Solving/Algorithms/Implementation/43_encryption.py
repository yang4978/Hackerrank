#https://www.hackerrank.com/challenges/encryption/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    rows = math.floor(math.sqrt(len(s)))
    cols = math.ceil(math.sqrt(len(s)))
    # M = []
    # for i in range(cols):
    #     M.append(''.join([s[j] for j in range(i,len(s),cols)]))
    # return ' '.join(M)

    return(' '.join(map(lambda x: s[x::cols], range(cols))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
