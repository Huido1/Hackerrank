#url: https://www.hackerrank.com/challenges/polar-coordinates/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath

n = complex(input())


print(cmath.polar(n)[0])
print(cmath.polar(n)[1])
