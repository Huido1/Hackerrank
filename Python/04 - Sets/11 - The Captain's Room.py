#url: https://www.hackerrank.com/challenges/py-the-captains-room/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = input().split()

A = set()
B = set()

for i in x:
    if i not in A:
        A.add(i)
    else:
        B.add(i)
        
a = A^B

for i in a:
    print (i)
