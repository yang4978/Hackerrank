#https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    
    if(year%4==0):
        if(year%100==0 and year%400!=0):
            leap = False;
        else:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))
