#url: https://www.hackerrank.com/challenges/piling-up/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

T = int(input())

for i in range(T):
    n = int(input())
    x = collections.deque(map(int, input().split()))
    while len(x) > 1 and x[0] >= x[1]:
        x.popleft()
    while len(x) > 1 and x[-1] >= x[-2]:
        x.pop()
    if len(x) <= 1:
        print("Yes")
    else:
        print("No")
