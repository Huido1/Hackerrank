#url: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

n, m = map(int, input().split())
d = collections.defaultdict(list)
list2 = []

for i in range (n):
    d[input()].append(i+1)
for i in range(m):
    list2.append(input())

for i in list2:
    if i in d:
        print(" ".join(map(str, d[i])))
    else:
        print(-1)
