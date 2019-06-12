#https://www.hackerrank.com/challenges/bigger-is-greater/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    i = len(w)-1
    while(i):
        if(w[i]>w[i-1]):
            j = w[i:].index(min([letter for letter in w[i:] if letter>w[i-1]]))+i
            w = list(w)
            w[i-1],w[j] = w[j],w[i-1]
            w = ''.join(w)
            return w[:i]+''.join(sorted(w[i:]))
        i -= 1

    return "no answer"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
