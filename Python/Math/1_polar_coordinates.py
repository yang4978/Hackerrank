#https://www.hackerrank.com/challenges/polar-coordinates/problem
import cmath
if __name__ == '__main__':
    print(*cmath.polar(complex(input())), sep='\n')
