#url: https://www.hackerrank.com/challenges/py-check-subset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for i in range(n):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    C = A-B
    if len(C) == 0:
        print (True)
    else:
        print (False)
