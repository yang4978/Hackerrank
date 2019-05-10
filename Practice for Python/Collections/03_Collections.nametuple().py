#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple
t = int(input());
student = namedtuple('Student',input().split());
print('%.2f' %(sum(float(student(*input().split()).MARKS) for _ in range(t))/t))
