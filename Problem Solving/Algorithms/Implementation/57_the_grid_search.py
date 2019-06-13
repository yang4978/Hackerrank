#https://www.hackerrank.com/challenges/the-grid-search/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    G_row = len(G)
    G_column = len(G[0])
    P_row = len(P)
    P_column = len(P[0])
    for i in range(G_row-P_row+1):
        for j in range(G_column-P_column+1):
            k = 0
            while(k<P_row):
                if(P[k]!=G[i+k][j:(j+P_column)]):
                    break
                k += 1
            if(k==P_row):
                return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
