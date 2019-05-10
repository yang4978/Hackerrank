#https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

import sys

if __name__ == '__main__':
    n = int(input());
    dict = {};
    for _ in range(n):
        s,num = input().split();
        dict[s] = num;

    lines = sys.stdin.readlines()
    for i in lines:
        name = i.strip();
        if (dict.get(name)):
            print(name,"=",dict[name],sep='');
        else:
            print("Not found");
    


