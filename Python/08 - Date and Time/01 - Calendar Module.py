#url: https://www.hackerrank.com/challenges/calendar-module/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

x,y,z = map(int, input().split())

print(calendar.day_name[calendar.weekday(z, x, y)].upper())
