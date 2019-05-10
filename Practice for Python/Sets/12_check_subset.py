#https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    t = int(input());
    for _ in range(t):
        length_A = int(input());
        A = set(map(int,input().split()))
        length_B = int(input());
        B = set(map(int,input().split()))
    
        """if(len(B.difference(A))==(length_B-length_A)):
            print ('True');
        else:
            print ('False');"""
        print (A.issubset(B))

