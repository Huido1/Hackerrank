#url: https://www.hackerrank.com/challenges/collections-counter/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

X = int(input())
num = list(map(int, input().split()))
N = int(input())
Counter = collections.Counter(num)

Revenue = 0

for i in range(N):
    tal, din = map(int, input().split())
    if Counter[tal]:
        Revenue += din
        Counter[tal] -= 1
        
print(Revenue)
