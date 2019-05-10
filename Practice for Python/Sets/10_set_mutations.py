#https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
s = set(map(int, input().split()))
times = int(input());
for _ in range(times):
    l = list(map(str,input().split()));
    s_mut = set(map(int,input().split()));
    if (l[0]=='update'):
        s.update(s_mut);
    elif (l[0]=='intersection_update'):
        s.intersection_update(s_mut);
    elif (l[0]=='difference_update'):
        s.difference_update(s_mut);
    elif (l[0]=='symmetric_difference_update'):
        s.symmetric_difference_update(s_mut)

print (sum(s))
