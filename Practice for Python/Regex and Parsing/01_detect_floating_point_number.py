#https://www.hackerrank.com/challenges/introduction-to-regex/problem
import re
for _ in range(int(input())):
    s = input()
    print(True if re.match(r'^[.+-]?[0-9]*\.[0-9]+$',s) else False )

