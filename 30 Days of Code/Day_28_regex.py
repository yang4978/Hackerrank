#https://www.hackerrank.com/challenges/30-regex-patterns/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    l = [];

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if re.match(r'[a-zA-Z\.]+@+gmail+\.+com',emailID):
            l.append(firstName)

    print('\n'.join(sorted(l)))
