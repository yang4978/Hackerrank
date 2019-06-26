#https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    result = 0
    num = [0]*201
    for i in expenditure[:d]:
        num[i] += 1
    
    for i in range(d,len(expenditure)):
        if(d%2):
            temp = d//2+1
            for j in range(201):
                temp -= num[j]
                if temp<=0:
                    median = j
                    break
        else:
            flag = 1
            temp = d//2+1
            for j in range(201):
                temp -= num[j]
                if temp-1<=0 and flag:
                    median = j
                    flag = 0
                if temp<=0:
                    median = (median+j)/2.0
                    break
        if expenditure[i]>=2*median:
            result += 1
        
        num[expenditure[i-d]] -= 1
        num[expenditure[i]] += 1
    
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
