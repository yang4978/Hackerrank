#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re
# s = input().strip()
# flag = 1
# if(re.search(r'([^aeiouAEIOU][aeiouAEIOU]{2,}[^aeiouAEIOU])',s)):
#     while(flag):
#         temp = re.search(r'([^aeiouAEIOU][aeiouAEIOU]{2,}[^aeiouAEIOU])',s)
#         if(temp):
#             flag = 1;
#             l = re.findall(r'[aeiouAEIOU]{2,}',temp.group(1)).pop()
#             print(l)
#             rubbish_0,rubbish_1,s = s.partition(l)
#             continue;
#         flag = 0;
# else:
#     print(-1)

match = re.findall(r'(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])',input(),re.I)
print(*match if match else [-1],sep='\n')

