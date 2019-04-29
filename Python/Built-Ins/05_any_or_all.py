#https://www.hackerrank.com/challenges/any-or-all/problem

n = int(input())
l = list(map(int,input().split()))
print(any(map(lambda x: str(x)==str(x)[::-1], l))) if (all(map(lambda x: x>0, l))) else print('False')
