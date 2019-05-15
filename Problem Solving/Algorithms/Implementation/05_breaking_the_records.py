#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_score = scores[0];
    min_score = scores[0];
    max_times = 0;
    min_times = 0;

    for i in scores:
        if(i>max_score):
            max_score = i;
            max_times += 1;
        if(i<min_score):
            min_score = i;
            min_times += 1;

    return [max_times,min_times];


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
