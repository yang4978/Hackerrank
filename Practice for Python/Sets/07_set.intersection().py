#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input());
s1 = set(map(int,input().split()));
m = int(input());
s2 = set(map(int,input().split()));
print (len(s1.intersection(s2)));
