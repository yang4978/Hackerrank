#https://www.hackerrank.com/challenges/two-pluses/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def twoPluses(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = 0
    for i in range(rows):
        for j in range(cols):
            limit_1 = min(i,rows-1-i,j,cols-1-j)
            size_1 = 0
            k = 0
            while(k<=limit_1):
                if( grid[i][j-k]=='G' 
                and grid[i-k][j]=='G' 
                and grid[i][j+k]=='G'
                and grid[i+k][j]=='G'):
                    size_1 = 1+4*k
                    for m in range(rows):
                        for n in range(cols):
                            size_2 = 0
                            if(m==i and n==j): continue
                            l = 0
                            limit_2 = min(m,rows-1-m,n,cols-1-n)
                            while(l<=limit_2):
                                if( grid[m][n-l]=='G' 
                                and grid[m-l][n]=='G' 
                                and grid[m][n+l]=='G'
                                and grid[m+l][n]=='G'):
                                    if(m==i and j-k<=n-l<=j+k):break
                                    if(m==i and j-k<=n+l<=j+k):break
                                    if(m-l==i and j-k<=n<=j+k):break
                                    if(m+l==i and j-k<=n<=j+k):break
                                    if(n-l==j and i-k<=m<=i+k):break
                                    if(n+l==j and i-k<=m<=i+k):break
                                    if(n==j and i-k<=m-l<=i+k):break
                                    if(n==j and i-k<=m+l<=i+k):break
                                    size_2 = 1+4*l
                                    l += 1
                                else:
                                    break  
                            result = max(result,size_1*size_2)
                    k += 1
                else:
                    break
             
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
