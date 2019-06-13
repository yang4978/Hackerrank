#https://www.hackerrank.com/challenges/lisa-workbook/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page = 1
    result = 0
    for i in arr:
        flag = 0
        while(i>0):
            if (1+flag*k)<=page<=(flag*k+min(i,k)):
                result += 1
            i -= k
            flag += 1
            page += 1
    #dict_page = {}
    #     while(i>0):
    #         dict_page[page] = [k for k in range(1+flag*k,1+flag*k+min(i,k))]
    #         i -= k
    #         flag += 1
    #         page += 1
    # for key,value in dict_page.items():
    #     if key in value:
    #         result += 1    
    # for key,value in dict_page.items():
    #     if key in value:
    #         result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
