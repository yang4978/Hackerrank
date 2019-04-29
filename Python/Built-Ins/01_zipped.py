#https://www.hackerrank.com/challenges/zipped/problem

m,n = map(int,input().split())
l = []
for _ in range(n):
    l.append(list(map(float,input().split())))
for i in zip(*l):
    print(sum(i)/n)
