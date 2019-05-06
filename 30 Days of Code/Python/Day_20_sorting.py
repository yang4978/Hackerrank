#https://www.hackerrank.com/challenges/30-sorting/problem

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
sum_swap = 0;
num_of_swaps = 1;
while(num_of_swaps!=0):
    num_of_swaps = 0;
    for j in range(n-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1] = a[j+1],a[j];
            num_of_swaps += 1;
    sum_swap += num_of_swaps;

print('Array is sorted in %d swaps.' %sum_swap);
print('First Element: %d' %a[0]);
print('Last Element: %d' %a[-1]);
