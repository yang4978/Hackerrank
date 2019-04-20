#https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    #con_num = [];
    max_num = 0;
    while (n!=0):
        if(n%2):
            num = 1;
            n = (n-1)/2;
            while (n%2):
                num += 1;
                n = (n-1)/2;
            #con_num.append(num);
            if(num>max_num):
                max_num = num;
        
        else:
            n=n/2;

    #print (max(con_num));
    print (max_num);


