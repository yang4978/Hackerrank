#https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re
for _ in range(int(input())):
    if(re.match(r'^[789][0-9]{9}$',input())):
        print("YES")
    else:
        print("NO")

