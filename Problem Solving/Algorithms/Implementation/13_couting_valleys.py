#https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = [0];
    count = 0;
    for i in range(n):
        if(s[i]=='U'):
            step = 1;
        else:
            step = -1;
        height.append(height[i]+step);
        if((height[i]*height[i+1]==0) and height[i]<0):
            count += 1;
    print(height);
    return count;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
