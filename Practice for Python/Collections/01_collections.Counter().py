#https://www.hackerrank.com/challenges/collections-counter/problem

import collections

if __name__ == '__main__':
    n = int(input());
    shoe_list = collections.Counter(map(int,input().split()));
    m = int(input());
    result = 0;
    for _ in range(m):
        size,price = map(int,input().split());
        if(size in shoe_list and shoe_list[size]>0):
            shoe_list[size] -= 1;
            result += price;
    print (result)
