#url: https://www.hackerrank.com/challenges/itertools-combinations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

A, B = input().split()

for i in range(1, int(B)+1):
    for j in itertools.combinations(sorted(A), i):
        print("".join(j))
