#https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
s,k = input().split()
print (*map(''.join,permutations(sorted(s),int(k))),sep='\n')
