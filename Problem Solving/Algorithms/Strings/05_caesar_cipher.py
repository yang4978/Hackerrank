#https://www.hackerrank.com/challenges/caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    s = list(s)
    for i in range(len(s)):
        if(65<=ord(s[i])<=90):
            s[i] = chr(ord(s[i])+k%26) if ord(s[i])+k%26 <=90 else chr(ord(s[i])+k%26-26)       
        elif(97<=ord(s[i])<=122):
            s[i] = chr(ord(s[i])+k%26) if ord(s[i])+k%26 <=122 else chr(ord(s[i])+k%26-26)
    return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
