#https://www.hackerrank.com/challenges/between-two-sets/problem

#!/bin/python3

import os
import sys

def gcd(a,b):
    temp = a%b
    while(temp):
        a = b
        b = temp
        temp = a%b
    return b

def lcd(a,b):
    return a*b//gcd(a,b)

def getTotalX(a, b):
    lcd_a = a[0]
    gcd_b = b[0]
    
    for i in a:
        lcd_a = lcd(lcd_a,i)
    
    for i in b:
        gcd_b = gcd(gcd_b,i)

    return sum([gcd_b%(lcd_a*i)==0  for i in range(1,gcd_b//lcd_a+1)]) 

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
