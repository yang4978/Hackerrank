#https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations
S,k = input().split()
S = sorted(S)
for i in range(1,int(k)+1):
    print('\n'.join([''.join(i) for i in combinations(S,i)]))

