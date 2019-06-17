#https://www.hackerrank.com/challenges/weighted-uniform-string/problem 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    s_num = list(map(lambda x:ord(x)-96,list(s)))
    weight = set(s_num)
    i = 0
    while i<len(s)-1:
        temp = s_num[i]
        while(s_num[i]==s_num[i+1]):
            temp += s_num[i+1]
            i += 1
            weight.add(temp)
            if(i==len(s)-1):
                break;  
        i += 1
    result = []
    for i in queries:
        result.append("Yes" if i in weight else "No")
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
