#https://www.hackerrank.com/challenges/compress-the-string/problem

s = input()
temp = 1;
s += '\n'
for i in range(len(s)-1):
    if(s[i+1]==s[i]):
        temp += 1;
    else:
        print('(%d, %s)' %(temp,s[i]),end=' ')
        temp = 1;
    

# from __future__ import print_function
# from itertools import *

# for i,j in groupby(map(int,list(raw_input()))):
#     print(tuple([len(list(j)), i]) ,end = " ")

