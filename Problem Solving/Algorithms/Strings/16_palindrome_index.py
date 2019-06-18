#https://www.hackerrank.com/challenges/palindrome-index/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
# def palindromeIndex(s):
#     s_reverse = s[::-1]
#     if(s==s_reverse):
#         return -1
#     len_s = len(s)
#     len_temp = len_s-1
#     for i in range(len_s):
#         temp = s[:i]+s[i+1:]
#         temp_i =s_reverse[:len_temp-i]+s_reverse[len_temp-i+1:]
#         if (temp==temp_i):
#         #if(temp[:(len_temp+1)//2-1:-1]==temp[:len_temp//2]):
#             return i
#     return -1

################### METHOD 2######################

# def find_mismatching_pair(s):
#     i = 0
#     j = len(s) - 1
#     while i < j and s[i] == s[j]:
#         i += 1
#         j -= 1
#     return i, j
    
    
# def is_palindrome(s):
#     i, j = find_mismatching_pair(s)
#     return True if j <= i else False
    
    
# def palindromeIndex(s):
#     i, j = find_mismatching_pair(s)
#     return -1 if j <= i else i if is_palindrome(s[i+1 : j+1]) else j

def palindromeIndex(s):
    i,j=0,len(s)-1
    while(i<j):
        if(s[i]!=s[j]):
            s1 = s[0:i+1] if (len(s)-2)//2==i else s[i:(len(s)-2)//2]
            s2 = s[:j+1:-1] if (len(s)-1)//2==j else s[j-1:(len(s)-1)//2:-1]
            if(s1==s2):
                return j
            else:
                return i
        i += 1
        j -= 1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
