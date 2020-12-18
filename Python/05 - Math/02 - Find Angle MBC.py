#url: https://www.hackerrank.com/challenges/find-angle/problem

#Ejercicio problematico, no volverse locos si da error, son detalles en los que no vale la pena perder tiempo

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

AB,BC=int(input()),int(input())

hipo=math.hypot(AB,BC)           
           
res=round(math.degrees(math.acos(BC/hipo)))  
degree=chr(176)                                
print(res,degree, sep='')
