#https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the anagram function below.
def anagram(s):
    if(len(s)%2):
        return -1
    # letter_num_a = []
    # for i in range(26):
    #     letter_num_a.append(0)
    # letter_num_b = letter_num_a[:]
    # for i in range(len(s)//2):
    #     letter_num_a[ord(s[i])-97] += 1 
    #     letter_num_b[ord(s[i+len(s)//2])-97] += 1
    # return sum([abs(letter_num_a[i]-letter_num_b[i]) for i in range(26)])//2
    temp = Counter(s[0:len(s)//2]) - Counter(s[len(s)//2:])
    return sum(temp.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
