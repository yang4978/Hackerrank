#https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    n = len(string)
    s = [string[i:i+k] for i in range(0,n,k)];
    for i in s:
        print(''.join(sorted(set(i),key=i.index)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
