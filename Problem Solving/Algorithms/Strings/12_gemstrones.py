#https://www.hackerrank.com/challenges/gem-stones/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the gemstones function below.
def gemstones(arr):
    # count = 0;
    # for i in set(arr[0]):
    #     flag = 1
    #     for j in range(1,len(arr)):
    #         if i not in arr[j]:
    #             flag = 0;
    #     if(flag):
    #         count += 1
    # return count
    return len(reduce(lambda x,y:set(x).intersection(set(y)),arr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
