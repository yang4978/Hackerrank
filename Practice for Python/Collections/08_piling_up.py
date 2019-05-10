#https://www.hackerrank.com/challenges/piling-up/problem

t = int(input());
for _ in range(t):
    n = int(input());
    num = list(map(int,input().split()));
    i = 0;
    while (i<n-1 and num[i]>=num[i+1]):
        i += 1;
    while (i<n-1 and num[i]<=num[i+1]):
        i += 1;
    print ('Yes') if i==n-1 else print('No')
