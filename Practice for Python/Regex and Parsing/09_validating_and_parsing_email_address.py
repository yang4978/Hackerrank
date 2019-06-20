#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import email.utils
import re
for _ in range(int(input())):
    temp = email.utils.parseaddr(input())
    if(re.match(r'^[A-Za-z][\w\.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$',temp[1])):
        print (email.utils.formataddr(temp))

