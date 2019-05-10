#https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input());
    dict = OrderedDict();
    for _ in range(n):
        key = input();
        if key not in dict:
            dict.update({key:1});
            continue;
        dict[key] += 1;
    print(len(dict.keys()));   
    print(*dict.values());
