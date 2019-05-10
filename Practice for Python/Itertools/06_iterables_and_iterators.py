#https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations
N = input();
a = [1 if 'a' in i else 0 for i in combinations(input().split(' '),int(input()))]
print (sum(a)/len(a))
