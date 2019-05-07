#https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

import math
if __name__ == '__main__':
    T = int(input());
    for _ in range(T):
        n = int(input());
        if(n==1):
            print('Not prime');
        elif(n==2):
            print('Prime');
        elif(n%2 == 0):
            print('Not prime');
        else:
            i = 3
            while(n%i and i<math.sqrt(n)+1):
                i += 2;
            if(i>math.sqrt(n)):
                print('Prime');
            else:
                print('Not prime');

