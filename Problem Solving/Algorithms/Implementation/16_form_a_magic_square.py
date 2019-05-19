#https://www.hackerrank.com/challenges/magic-square-forming/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def calculateAllMagicSqure():
    num = list(range(1,10));
    arr = [];
    arr_list = [];
    for i_1 in num:
        arr.append(i_1);
        for i_2 in num:
            if(i_2==i_1):
                continue;
            arr.append(i_2)
            for i_3 in num:
                if((i_1+i_2+i_3)!=15 or i_3==i_1 or i_3==i_2):
                    continue;   
                arr.append(i_3);
                for i_4 in num:
                    if(i_4==i_1 or i_4==i_2 or i_4==i_3):
                        continue;
                    arr.append(i_4);
                    for i_5 in num:
                        if(i_5==i_1 or i_5==i_2 or i_5==i_3 or i_5==i_4):
                            continue
                        arr.append(i_5);
                        for i_6 in num:
                            if((i_4+i_5+i_6)!=15 or i_6==i_1 or i_6==i_2 or i_6==i_3 or i_6==i_4 or i_6==i_5):
                                continue; 
                            arr.append(i_6);
                            for i_7 in num:
                                if((i_1+i_4+i_7)!=15 or (i_3+i_5+i_7)!=15 or i_7==i_1 or i_7==i_2 or i_7==i_3 or i_7==i_4 or i_7==i_5 or i_7==i_6):
                                    continue; 
                                arr.append(i_7);
                                for i_8 in num:
                                    if((i_2+i_5+i_8)!=15 or i_8==i_1 or i_8==i_2 or i_8==i_3 or i_8==i_4 or i_8==i_5 or i_8==i_6 or i_8==i_7):
                                        continue; 
                                    arr.append(i_8);
                                    for i_9 in num:    
                                        if(((i_3+i_6+i_9)!=15) or ((i_7+i_8+i_9)!=15) or ((i_1+i_5+i_9)!=15)  or i_9==i_1 or i_9==i_2 or i_9==i_3 or i_9==i_4 or i_9==i_5 or i_9==i_6 or i_9==i_7 or i_9==i_8):
                                            continue;               
                                        arr.append(i_9);
                                        arr_list.append(arr[:]);
                                        arr.remove(i_9);
                                    arr.remove(i_8);
                                arr.remove(i_7);
                            arr.remove(i_6);
                        arr.remove(i_5);
                    arr.remove(i_4);
                arr.remove(i_3);                       
            arr.remove(i_2);
        arr.remove(i_1);
    return arr_list;
                                       
                                        


def formingMagicSquare(s):
    arr_list = calculateAllMagicSqure();
    min_sum = 100;
    s_flatten = [n for i in s for n in i];
    for i in range(len(arr_list)):
        temp_sum = 0;
        for j in range(len(s_flatten)):
            temp_sum += abs(arr_list[i][j]-s_flatten[j])
        if (temp_sum<min_sum):
            min_sum = temp_sum;
    return (min_sum);

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
