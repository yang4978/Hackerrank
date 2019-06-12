#https://www.hackerrank.com/challenges/acm-icpc-team/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    print(int(topic[0],2))
    list_result=[];
    for i in range(len(topic)):
        for j in range(i+1,len(topic)):
            arrange = int(topic[i],2)|int(topic[j],2);
            result = str(bin(arrange)).count('1')
            list_result.append(result);
    return (max(list_result),list_result.count(max(list_result)))
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
