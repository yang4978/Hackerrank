#https://www.hackerrank.com/challenges/find-digits/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    temp_n = n;
    count = 0;
    power = len(str(n))-1;
    while(power>=0):
        num = temp_n//pow(10,power);
        temp_n = temp_n%pow(10,power);    
        if(num!=0 and n%num==0):
            count += 1;
        power -= 1;
    return count;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
