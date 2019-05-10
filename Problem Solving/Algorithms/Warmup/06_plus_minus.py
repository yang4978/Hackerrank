#https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    num_pos = 0;
    num_neg = 0;
    num_zero = 0;

    for i in arr:
        if i > 0:
            num_pos +=1;
        elif i < 0:
            num_neg +=1;
        else :
            num_zero +=1;
    print (num_pos/len(arr));
    print (num_neg/len(arr));
    print (num_zero/len(arr));

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
