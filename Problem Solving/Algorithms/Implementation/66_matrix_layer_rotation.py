#https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    #dict_matrix = {}
    rows = len(matrix)
    columns = len(matrix[0])
    for layer in range(min(rows,columns)//2):
        layer_r = r%(rows*2+columns*2-4-8*layer)
        while(layer_r):
            temp = matrix[layer][columns-layer-1]
            for j in range(columns-layer-2,layer-1,-1):                
                temp,matrix[layer][j] = matrix[layer][j],temp
            for i in range(layer+1,rows-layer):
                temp,matrix[i][layer] = matrix[i][layer],temp
            for j in range(layer+1,columns-layer):
                temp,matrix[rows-1-layer][j] = matrix[rows-1-layer][j],temp
            for i in range(rows-layer-2,layer-1,-1):
                temp,matrix[i][columns-1-layer] = matrix[i][columns-1-layer],temp
            #matrix[layer][columns-layer-1] = temp

            #     if(i>layer):
            #         dict_matrix[i,layer] = matrix[i][layer] 
            #     if(i<rows-layer-1):
            #         dict_matrix[i,columns-1-layer] = matrix[i][columns-1-layer]
            # for j in range(layer,columns-layer):                
            #     if(j<columns-layer-1):
            #         dict_matrix[layer,j] = matrix[layer][j]
            #     if(j>layer):    
            #         dict_matrix[rows-1-layer,j] = matrix[rows-1-layer][j]

            # for i in range(layer,rows-layer):
            #     if(i>layer):
            #         matrix[i][layer] = dict_matrix[i-1,layer]
            #     if(i<rows-layer-1):
            #         matrix[i][columns-1-layer] = dict_matrix[i+1,columns-1-layer]
            # for j in range(layer,columns-layer):                
            #     if(j<columns-layer-1):
            #         matrix[layer][j] = dict_matrix[layer,j+1]
            #     if(j>layer):    
            #         matrix[rows-1-layer][j] = dict_matrix[rows-1-layer,j-1]
            
            layer_r -= 1

    for i in matrix:
        print(*i)

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
