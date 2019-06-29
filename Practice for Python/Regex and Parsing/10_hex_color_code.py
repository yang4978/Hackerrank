#https://www.hackerrank.com/challenges/hex-color-code/problem

import re
for _ in range(int(input())):
    temp = re.findall(r'#[0-9a-fA-F]{3}(?=[;,)])|#[0-9a-fA-F]{6}(?=[;,)])',input())
    for i in temp:
        print(i)

