#https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if (year<=1917):
        if(year%4):
            return "13.09.%d" %year;
        else:
            return "12.09.%d" %year;
    elif (year>=1919):
        if(year%400==0):
            return "12.09.%d" %year;
        elif(year%100==0):
            return "13.09.%d" %year;
        elif(year%4==0):
            return "12.09.%d" %year;
        else:
            return "13.09.%d" %year;
    else:
        return "26.09.1918"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
