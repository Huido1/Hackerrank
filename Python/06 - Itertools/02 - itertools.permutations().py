#url: https://www.hackerrank.com/challenges/itertools-permutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

A, B = input().split()
res = list(itertools.permutations(A, int(B)))
res.sort()

[print("".join (i)) for i in res]
