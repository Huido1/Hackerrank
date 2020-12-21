#url: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

N = int(input())
Column = input().split()

Suma = 0
for i in range(N):
    Estudiante = collections.namedtuple("Estudiante", Column)
    Column1, Column2, Column3, Column4 = input().split()
    Estudiantes = Estudiante(Column1, Column2, Column3, Column4)
    Suma += int(Estudiantes.MARKS)
Average = Suma/N

print(Average)
