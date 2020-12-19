#url: https://www.hackerrank.com/challenges/itertools-product/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*itertools.product(A, B))           #No olvidarse el "*" para cumplir con el formato que pide el ejercicio
