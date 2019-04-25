#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict
fruit_net_price = OrderedDict();
n = int(input());
for _ in range(n):
    s = input().split();  
    if(' '.join(s[0:-1]) not in fruit_net_price):
        fruit_net_price[' '.join(s[0:-1])] = int(s[-1]);
    else:
        fruit_net_price[' '.join(s[0:-1])] += int(s[-1]);

for i in fruit_net_price.keys():
    print('%s %d' %(i,fruit_net_price[i]));

