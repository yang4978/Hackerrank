#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

import collections
if __name__ == '__main__':
    n,m = map(int,input().split());
    d = collections.defaultdict(list)
    for i in range(1,n+1):
        d[input()].append(i);
    for i in range(m):
        result = d.get(input(),-1);
        if(result == -1):
            print('-1');
        else:
            print(' '.join(map(str,result)))


