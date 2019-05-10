#https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == '__main__':
    n = int(input());
    stamp = set();
    for _ in range(n):
        stamp.add(input())
    print(len(stamp));


