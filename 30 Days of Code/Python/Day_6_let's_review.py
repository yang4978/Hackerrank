#https://www.hackerrank.com/challenges/30-review-loop/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    t = int(input());
    for i in range(t):
        s = input();
        s_1 = [];
        s_2 = [];
        for m in range(len(s)):
            if(m%2 == 0):
                s_1.append(s[m]);
            else:
                s_2.append(s[m]);
        s_1 = ''.join(s_1);
        s_2 = ''.join(s_2);
        print(s_1,s_2);
