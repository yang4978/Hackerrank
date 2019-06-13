#https://www.hackerrank.com/challenges/the-time-in-words/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    hour = [0,'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
    minute = [' o\' clock','one minute','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
    minute += [minute[20]+' '+minute[i] for i in range(1,10)]
    minute =minute[0:2]+[minute[i]+' minutes' for i in range(2,30)]
    minute[15] = 'quarter'
    minute.append('half')
    minute = minute[0:1]+[minute[i]+' past ' for i in range(1,31)]+[minute[30-i]+' to ' for i in range(1,30)]
    if(0<int(m)<=30):
        return minute[int(m)]+hour[int(h)]
    elif(int(m)>30):
        return minute[int(m)]+hour[int(h)+1]
    else:
        return hour[int(h)]+minute[0]

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
