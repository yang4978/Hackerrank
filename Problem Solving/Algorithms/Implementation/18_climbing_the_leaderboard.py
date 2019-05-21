#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    leaderboard = sorted(set(scores));
    leaderboard.reverse()
    scores_index = len(leaderboard)-1;
    alice_index = 0;
    result = [];
    while(alice_index<len(alice)):
        if(scores_index == 0):
            result.append(1);
            alice_index += 1;
            continue;

        if(alice[alice_index]<leaderboard[len(leaderboard)-1]):
            result.append(len(leaderboard)+1);
            alice_index += 1;
        elif(alice[alice_index]<leaderboard[scores_index-1]):
            result.append(scores_index+1);
            alice_index += 1;
        else:
            scores_index -= 1;


    

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
