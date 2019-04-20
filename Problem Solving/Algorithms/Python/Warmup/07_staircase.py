#https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="");
        for j in range (i+1):
            print("#",end="");
        print("\n",end="");


if __name__ == '__main__':
    n = int(input())

    staircase(n)
