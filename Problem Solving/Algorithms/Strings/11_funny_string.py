#https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    diff = [abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1)]
    for i in range(len(diff)//2):
        if(diff[i]!=diff[len(diff)-1-i]):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
