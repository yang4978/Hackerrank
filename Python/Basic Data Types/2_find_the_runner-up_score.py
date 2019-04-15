#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max_num = arr.count(max(arr));

    for i in range(max_num):
        arr.remove(max(arr));
    
    print(max(arr));

