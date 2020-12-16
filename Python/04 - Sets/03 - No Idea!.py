#url: https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()
arr = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))          #Se crean los sets

Felicidad = 0

for i in arr:
    if i in A:
        Felicidad += 1
    elif i in B:
        Felicidad -= 1
    else:                                   #Esta linea en realidad podria no ir, pero para aclarar mas la sintaxis la dejo. Las otras dos cumplen con el contador.
        Felicidad += 0
        
print(Felicidad)
