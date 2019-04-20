#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
times = int(input());
for _ in range(times):
    l = list(map(str,input().split()));
    if (l[0]=='pop'):
        s.pop();
    elif (l[0]=='remove'):
        if(int(l[1]) in s):
            s.remove(int(l[1]))
    elif (l[0]=='discard'):
        s.discard(int(l[1]))

print (sum(s))
