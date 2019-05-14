#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    lis = [0,1]
    [lis.append(lis[i-1]+lis[i-2]) for i in range(2,n)]
    return (lis[0:n])
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
