//https://www.hackerrank.com/challenges/maximum-palindromes/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#
def cal_mmi_mod(x,n):
    r = 1;
    x = x%1000000007
    while(n):
        if(n%2):
            r=(r*x)%1000000007
        x=(x*x)%1000000007
        n = n//2
    return r

#def initialize(s):
    
    # This function is called once before all queries.

#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def answerQuery(l, r):
    count = 0
    total_pair = 0
    div = 1
    for i in range(26):
        string_count = dict[r][i] - dict[l-1][i]
        count += string_count%2
        div = ((div%1000000007)*factorial_mmi[string_count//2])%1000000007
        total_pair += string_count//2

    result = (max(1,count) * factor[total_pair])*(div%1000000007)    
    return result%1000000007
    # Return the answer for this query modulo 1000000007.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    dict = {0:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    for i in range(1,len(s)+1):
        dict[i] = dict[i-1][:]
        dict[i][ord(s[i-1])-97] += 1

    factorial_mmi = {0:1,1:1}
    for i in range(2,50001):
        factorial_mmi[i] = ((cal_mmi_mod(i,1000000005)%1000000007)*(factorial_mmi[i-1]%1000000007))%1000000007

    factor = {0:1,1:1}
    for i in range(2,50001):
        factor[i] = ((i%1000000007)*(factor[i-1]%1000000007))%1000000007
    
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
