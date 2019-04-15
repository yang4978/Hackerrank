#https://www.hackerrank.com/challenges/py-if-else/problem

#!/bin/python3

n = int(input())
if((n%2==0) and (2<=n<=5 or n>20)):
    print ("Not Weird");
else:
    print ("Weird");
