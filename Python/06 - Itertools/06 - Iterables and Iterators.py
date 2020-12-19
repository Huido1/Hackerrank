#url: https://www.hackerrank.com/challenges/iterables-and-iterators/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

N = int(input())
J = input().split()
K = int(input())

c = list(itertools.combinations(J, K))
m=0
for i in c:
    if "a" in i:
        m += 1

print(m/len(c))
