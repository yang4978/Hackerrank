#https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_type = [];
    pair_num = 0;
    """for i in ar:
        if i not in sock_type:
            sock_type.append(i);"""
    
    sock_type = list(set(ar));

    for i in sock_type:
        pair_num += ar.count(i)//2;
    return pair_num;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
