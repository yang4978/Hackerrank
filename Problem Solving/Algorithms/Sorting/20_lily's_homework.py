#https://www.hackerrank.com/challenges/lilys-homework/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def lilysHomework(arr):
    # swap_incre = 0
    # swap_decre = 0
    # arr_incre_sort = sorted(arr)
    # num_incre = [arr_incre_sort.index(i) for i in arr]
    # num_decre = [len(arr)-1-i for i in num_incre]

    # for i in range(len(num_incre)):
    #     if(num_incre[i]!=i):
    #         j = num_incre.index(i)
    #         temp = num_incre[i]
    #         num_incre[i] = i
    #         num_incre[j] = temp
    #         swap_incre += 1

    #     if(num_decre[i]!=i):
    #         j = num_decre.index(i)
    #         temp = num_decre[i]
    #         num_decre[i] = i
    #         num_decre[j] = temp
    #         swap_decre += 1
    #         print(num_decre)

    #return min(swap_incre,swap_decre)
    arr_reverse = arr[:]
    len_arr = len(arr)
    arr_dict = {}
    arr_dict_reverse = {}
    arr_sorted = sorted(arr)
    arr_sorted_reverse = arr_sorted[::-1]
    for i in range(len_arr):
        arr_dict[arr[i]] = i 
        arr_dict_reverse[arr_reverse[i]] = i

    result = 0
    result_reverse = 0
    for i in range(len_arr):
        if(arr[i]!=arr_sorted[i]):
            result +=1
            arr_dict[arr[i]] = arr_dict[arr_sorted[i]]
            arr[i],arr[arr_dict[arr[i]]] = arr_sorted[i],arr[i]
        
        if(arr_reverse[i]!=arr_sorted_reverse[i]):
            result_reverse +=1
            arr_dict_reverse[arr_reverse[i]] = arr_dict_reverse[arr_sorted_reverse[i]]
            arr_reverse[i],arr_reverse[arr_dict_reverse[arr_reverse[i]]] = arr_sorted_reverse[i],arr_reverse[i]

    return min(result,result_reverse)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
