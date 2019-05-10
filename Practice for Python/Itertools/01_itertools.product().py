#https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product
print (*product(list(map(int,input().split())),list(map(int,input().split()))))
