#https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    Count_num = ()
    #calculate letter occurrence of each substring
    for i in range(1,len(s)):
        Count_num +=tuple([dict(Counter(s[j:i+j])) for j in range(len(s)-i+1)])
    
    count = 0
    # since Counter type are nont hashable, we have to count each item in Count_num
    # Generally, if one letter_occurrence has appeared n times, it means we can have
    # n!/(n-2)!/(2) combinations, but because in Count_num, they appears also n times,
    # so we have to divide n to get right result
    for i in Count_num:
        num = Count_num.count(i)
        count += math.factorial(num)//2//math.factorial(max(1,num-2))/num
        # max(1,num-2) in case of num=1
    return int(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
