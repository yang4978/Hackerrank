#https://www.hackerrank.com/challenges/bear-and-steady-gene/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the steadyGene function below.
def steadyGene(gene):
    n = len(gene)
    gene_num = {}
    gene_name = 'CGTA'
    num_C = gene.count('C')-n//4
    num_G = gene.count('G')-n//4
    num_T = gene.count('T')-n//4
    num_A = gene.count('A')-n//4
    # C = Counter(gene)
    # num_C = C['C']-n//4
    # num_G = C['G']-n//4
    # num_T = C['T']-n//4
    # num_A = C['A']-n//4
    # gene_length = (abs(num_C)+abs(num_G)+abs(num_T)+abs(num_A))//2
    # for i in range(gene_length,n):
    #     for j in gene_name:
    #         gene_num[j]=0
    #     for j in range(n-i+1):
    #         if(j==0):
    #             for k in gene[:i]:
    #                 gene_num[k] += 1
    #         else:
    #             gene_num[gene[j-1]] -= 1
    #             gene_num[gene[j+i-1]] += 1
    #         if(gene_num['C']>=num_C and gene_num['G']>=num_G and gene_num['T']>=num_T and gene_num['A']>=num_A):
    #             return i
    gene_length = (abs(num_C)+abs(num_G)+abs(num_T)+abs(num_A))//2
    if(not gene_length):
        return 0
    for i in gene_name:
        gene_num[i]=0
    left = 0
    right = gene_length-1
    min_length = n
    for i in gene[:gene_length]:
        gene_num[i] += 1
    while(left<=right and right<n-1):
        if(gene_num['C']>=num_C and gene_num['G']>=num_G and gene_num['T']>=num_T and gene_num['A']>=num_A):
            min_length = min(right-left+1,min_length)
            gene_num[gene[left]] -= 1
            left += 1
        else:
            right += 1
            gene_num[gene[right]] += 1

    return min_length
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
