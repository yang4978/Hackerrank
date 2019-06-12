#https://www.hackerrank.com/challenges/queens-attack-2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    result = 2*n-2+min(n-c_q,r_q-1)+min(n-c_q,n-r_q)+min(c_q-1,r_q-1)+min(c_q-1,n-r_q);
    num_left =0;
    num_right=0;
    num_up=0;
    num_down=0;
    num_lup=0;
    num_ldown=0;
    num_rup=0;
    num_rdown=0;
    for i in range(k):
        x = obstacles[i][0];
        y = obstacles[i][1];
        if(x==r_q and y>c_q):
            num_up = max(num_up,(n-y+1));
        if(x==r_q and y<c_q):
            num_down = max(num_down,y);
        if(y==c_q and x>r_q):
            num_right = max(num_right,(n-x+1));
        if(y==c_q and x<r_q):
            num_left = max(num_left,x);

        if(abs(x-r_q)==abs(y-c_q)):
            if(y>c_q and x<r_q):
                num_lup = max(num_lup,min(n-y,x-1)+1);
            if(y>c_q and x>r_q):
                num_rup = max(num_rup,min(n-x,n-y)+1);
            if(y<c_q and x<r_q):
                num_ldown = max(num_ldown,min(x-1,y-1)+1);
            if(y<c_q and x>r_q):
                num_rdown = max(num_rdown,min(y-1,n-x)+1);
    return result-num_down-num_up-num_left-num_right-num_ldown-num_lup-num_rdown-num_rup;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
