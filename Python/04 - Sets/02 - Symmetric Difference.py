#url: https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
M1 = set(map(int, input().split()))

N = int(input())
N1 = set(map(int, input().split()))

a = M1^N1

print("\n".join(map(str, sorted(a))))
