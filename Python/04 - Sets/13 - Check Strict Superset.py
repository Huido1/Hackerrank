#url: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = set(input().split(" "))
n = int(input())

j = 0

for i in range(n):
    x = set(input().split(" "))
    a = N.issuperset(x)
    if a == True:
        j += 1

print (j == n)
