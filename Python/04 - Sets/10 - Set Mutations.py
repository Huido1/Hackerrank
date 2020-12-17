#url: https://www.hackerrank.com/challenges/py-set-mutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    x, y = input().split()
    S = set(map(int, input().split()))
    if x == "update":
        s.update(S)
    elif x == "intersection_update":
        s.intersection_update(S)
    elif x == "difference_update":
        s.difference_update(S)
    elif x == "symmetric_difference_update":
        s.symmetric_difference_update(S)
print(sum(s))
