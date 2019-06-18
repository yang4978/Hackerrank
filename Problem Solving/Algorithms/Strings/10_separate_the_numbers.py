#https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    if(s[0]=='0'):
        print("NO")
        return
    for i in range(1,len(s)//2+1):
        num = int(''.join(s[:i]))
        temp = ''
        while(len(temp)<len(s)):
            temp += str(num)
            num += 1
        if(temp==s):
            print("YES",s[:i])
            return 
    print ("NO")

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
