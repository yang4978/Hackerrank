#https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    #correct answer
    return ' '.join(i.capitalize() for i in s.split(" "))
    
    #my own code
    """num_of_space = 0;
    s = [i for i in s];
    s_split = [i for i in s];
    s_split[0] = s_split[0].upper();
    while(s.count(" ")):
        temp_index = s.index(" ");
        num_of_space += 1;
        s.remove(" ");
        index = temp_index + num_of_space;       
        s_split[index]=s_split[index].upper();
    return ''.join(s_split)"""

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
