#url: https://www.hackerrank.com/challenges/py-collections-deque/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

n = int(input())
d = collections.deque()

for i in range (n):
        x = input().split(" ")
        command = x[0]                              
        if command == "append":                     
            d.append(int(x[1]))
        elif command == "pop":
            d.pop()
        elif command == "popleft":
            d.popleft()
        elif command == "appendleft":
            d.appendleft(int(x[1]))
            
print(*d)
    
