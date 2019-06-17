#https://www.hackerrank.com/challenges/two-characters/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    letter =list(set(s))
    max_length = 0;
    for i in range(len(letter)):
        for j in range(i+1,len(letter)):
            temp = s
            for k in range(len(letter)):
                if k!=i and k!=j:
                    while(re.search(letter[k],temp)):
                        temp = re.sub(letter[k],'',temp)
            print(temp)
            if(re.search(r'(\w)\1',temp)):
                continue;
            else:
                max_length = max(max_length,len(temp))
    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
