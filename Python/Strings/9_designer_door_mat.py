#https://www.hackerrank.com/challenges/designer-door-mat/problem

if __name__ == '__main__':
    parameter = list(map(int,input().split()));
    N = parameter[0];
    M = parameter[1];
    for i in range(N//2):
        c = '.|.'
        print((c*(2*i+1)).center(M,'-'));
    
    print('WELCOME'.center(M,'-'));
    
    for i in range(N//2,0,-1):
        c = '.|.'
        print((c*(2*i-1)).center(M,'-'));

