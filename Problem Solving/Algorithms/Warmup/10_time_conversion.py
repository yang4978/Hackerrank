#https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    n = len(s);
    if s[n-2] == 'A':
        if s[0:2] == '12':
            result = '00'+s[2:(n-2)];
        else:
            result = s[0:(n-2)];
    else:
        if s[0:2] == '12':
            result = s[0:(n-2)];
        else:
            result = str(int(s[0:2])+12)+s[2:(n-2)];
    return result;

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
