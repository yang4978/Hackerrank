#https://www.hackerrank.com/challenges/30-bitwise-and/problem

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        # max = 0

        # for i in range(1,n):
        #     for j in range(i+1,n+1):
        #         temp = i&j;
        #         max = temp if max<temp<k else max
        #         if(max==k-1):
        #             break;
        # print(max)
        print(k-1 if ((k-1) | k) <= n else k-2)
