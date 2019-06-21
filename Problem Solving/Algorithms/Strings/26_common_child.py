#https://www.hackerrank.com/challenges/common-child/copy-from/111541300

#!/bin/python3

import math
import os
import random
import re
import sys

def commonChild(s1, s2):
    len_s = len(s1)
    if(len_s):
        CC = [[0]*(len_s+1) for i in range(len_s+1)]
        for i in range(1,len_s+1):
            for j in range(1,len_s+1):
                if(s1[i-1]==s2[j-1]):
                    CC[i][j] = CC[i-1][j-1]+1
                else:
                    CC[i][j] = CC[i-1][j] if(CC[i-1][j]>CC[i][j-1]) else CC[i][j-1]
        return CC[len_s][len_s]  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

