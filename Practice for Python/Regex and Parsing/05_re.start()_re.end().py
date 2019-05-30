#https://www.hackerrank.com/challenges/re-start-re-end/problem

import re
S = input()
k = input()
if(re.search(k,S)):
    temp = 0;
    while(re.search(k,S)):
        i = re.search(k,S)
        print ('(%d, %d)'%(i.start()+temp,i.end()-1+temp))
        S = S[i.start()+1:]
        temp = temp+i.start()+1

else:
    print('(-1, -1)')
