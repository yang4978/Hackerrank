#https://www.hackerrank.com/challenges/maximize-it/problem

from functools import reduce
def fn(lists):
    def myfunc(list1, list2):
        return [i+j for i in list1 for j in list2]
    return reduce(myfunc, lists)

n,M = input().split()
l = [];
for _ in range(int(n)):
    l.append([i**2 for i in list(map(int,input().split()))[1:]])
print (max([i%int(M) for i in fn(l)]))

# from itertools import product

# K,M = map(int,input().split())
# N = (list(map(int, input().split()))[1:] for _ in range(K))
# results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
# print(max(results))
