#https://www.hackerrank.com/challenges/non-divisible-subset/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    num_mod = [i%k for i in S];
    print(num_mod)
    mod_0 = min(num_mod.count(0),1);
    result = mod_0;
    for i in range(1,k//2+1):
        result += max(num_mod.count(i),num_mod.count(k-i));
    if(k%2==0):
        result += min(num_mod.count(k//2),1) - num_mod.count(k//2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()
