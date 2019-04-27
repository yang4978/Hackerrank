#https://www.hackerrank.com/challenges/incorrect-regex/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    t = int(input());
    for _ in range(t):
        s = input();
        try:
            re.compile(s)
            print("True");
        except re.error:
            print("False");
    
