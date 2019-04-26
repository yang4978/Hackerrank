#https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
mm,dd,yy = map(int,input().split())
weekday = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print (weekday[calendar.weekday(yy,mm,dd)])

#print(list(calendar.day_name)[calendar.weekday(yy,mm,dd)].upper())

