#url: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

A, B = input().split()

for i in itertools.combinations_with_replacement(sorted(A), int(B)):
    print("".join(i))
