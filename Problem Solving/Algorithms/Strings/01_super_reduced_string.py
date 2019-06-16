#https://www.hackerrank.com/challenges/reduced-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    # s = list(s)
    # temp=[1];
    # while(temp):
    #     temp = [];
    #     i = 0
    #     while i < len(s)-1:
    #         if(s[i]==s[i+1]):
    #             temp.append(i)
    #             i += 1
    #         i += 1
       
    #     for i in range(len(temp)):
    #         s.pop(temp[i]-2*i)
    #         s.pop(temp[i]-2*i)

    # return ''.join(s) if s!=[] else "Empty String"

    while(re.search(r'(.)\1',s)):
        s = re.sub(r'(.)\1','',s)

    return s if s!='' else "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
