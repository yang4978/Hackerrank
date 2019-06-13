#https://www.hackerrank.com/challenges/cavity-map/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    position = []
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            if(grid[i][j]>max(
                grid[i-1][j],
                grid[i][j-1],
                grid[i][j+1],
                grid[i+1][j],
            )):
                position.append([i,j])
    for i,j in position:
        grid[i] = grid[i][0:j]+'X'+grid[i][j+1:]
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
