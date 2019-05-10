#https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict
from collections import Counter


if __name__ == '__main__':
    ### using Counter
    s_count = Counter(input())
    for i in sorted(sorted(s_count.keys()),key = lambda x:s_count[x],reverse=True)[:3]:
        print("%s %d" %(i,s_count[i]))

    ### Using OrderedDict

    # letter = OrderedDict();
    # for i in range(ord('a'),ord('z')+1):
    #     letter[chr(i)] = 0;

    # for i in s:
    #     letter[i] += 1;
    # M_letter = [];
    # M_value = [];
    # for i in range(3):
    #     M_letter.append(max(letter,key=letter.get));
    #     M_value.append(letter[M_letter[i]]);
    #     letter.pop(M_letter[i]);
    #     print("%s %d" %(M_letter[i],M_value[i]))



