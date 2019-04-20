#https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == '__main__':
    array_dim = list(map(int,input().split()));
    arr = list(map(int,input().split()));
    A = set(map(int,input().split()));
    B = set(map(int,input().split()));
    """happiness = 0;
    for i in arr:
        if i in A:
            happiness += 1;
        if i in B:
            happiness -= 1;
    print (happiness);"""

    print (sum([(i in A) - (i in B) for i in arr]))



