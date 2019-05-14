#https://www.hackerrank.com/challenges/apple-and-orange/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    num_apple = 0;
    num_oranges = 0;
    for i in apples:
        if( s<=a+i<=t ):
            num_apple += 1;
    print(num_apple);
    
    for i in oranges:
        if ( s<=b+i<=t ):
            num_oranges += 1;
    print(num_oranges);


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
