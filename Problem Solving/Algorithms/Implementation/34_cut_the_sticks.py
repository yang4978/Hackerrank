#https://www.hackerrank.com/challenges/cut-the-sticks/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    length_type = list(set(arr));
    length_type.sort();
    length_num = [arr.count(i) for i in length_type];
    result = [sum(length_num[i:]) for i in range(len(length_num))];
    return result;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
