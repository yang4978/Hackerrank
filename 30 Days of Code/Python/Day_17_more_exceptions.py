#https://www.hackerrank.com/challenges/30-more-exceptions/problem

class Calculator(Exception):
    def __init__(self):
        self = 0;

    def power(self,n,p):
        if(n<0 or p<0):
            raise Exception("n and p should be non-negative")
        return pow(n,p);

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
