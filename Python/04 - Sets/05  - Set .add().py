#url: https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = set()
for word in range(n):
    A.add(str(input()))
    
print(len(A))
