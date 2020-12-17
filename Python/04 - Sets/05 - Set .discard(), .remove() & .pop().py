#url: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    x = input().split()
    command = x[0]
    if command == "remove":
        s.remove(int(x[1]))
    elif command == "discard":
        s.discard(int(x[1]))
    elif command == "pop":
        s.pop()
        
print(sum(s))
