#https://www.hackerrank.com/challenges/py-check-strict-superset/problem

if __name__ == '__main__':
    A = set(map(int,input().split()));
    n = int(input());
    i = 1;
    while(i<=n):
        temp = set(map(int,input().split()));
        if (temp.issubset(A)==0 or len(temp)==len(A)):
            print ('False');
            break;
        i += 1;
    if (i==(n+1)):
        print('True');
