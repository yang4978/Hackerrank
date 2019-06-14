#https://www.hackerrank.com/challenges/bomber-man/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
  rows = len(grid)
  columns = len(grid[0])
  if(n==1):
    return grid
  elif(n%2==0):
    return ['O'*columns for i in range(rows)]
  else:
    n = 1+(n+1)//2%2
    dict_grid = {}
    for i in range(rows):
      grid[i] = list(grid[i])
    while(n):
      for i in range(rows):       
        for j in range(columns):
          dict_grid[i,j] = 'O'
    
      for i in range(rows):
        for j in range(columns):
          if(grid[i][j]=='O'):
            dict_grid[i,j] ='.'
            if(i>0):
              dict_grid[i-1,j] = '.'
            if(i<rows-1):
              dict_grid[i+1,j] = '.'
            if(j>0):
              dict_grid[i,j-1] = '.'
            if(j<columns-1):
              dict_grid[i,j+1] = '.'

      for key,values in dict_grid.items():
        grid[key[0]][key[1]] = values

      n -= 1
      #print(*grid,sep='\n')

    return [''.join(grid[i]) for i in range(rows)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
