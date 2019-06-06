#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def rev(num):
    temp = list(map(str,str(num)))
    temp.reverse()
    return (int(''.join(temp)))

def beautifulDays(i, j, k):
    result = 0;
    for num in range(i,j+1):
        if(((num-rev(num))%k)==0):
            result += 1;
    return result;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
