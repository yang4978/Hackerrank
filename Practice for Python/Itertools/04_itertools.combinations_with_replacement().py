#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/

from itertools import combinations_with_replacement
S,k = input().split()
print('\n'.join([''.join(i) for i in combinations_with_replacement(sorted(S),int(k))]))

