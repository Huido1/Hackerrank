#url: https://www.hackerrank.com/challenges/nested-list/problem

n = int(input())

PythonStudents = []
Notas = []

for i in range(n):
    nombre = input()
    nota = float(input())
    PythonStudents.append([nombre, nota])
    Notas.append(nota)
    
a = sorted(set(Notas))[1]                      #Se crea una lista vacia y se rellena con el formato de PythonStudents que pide el ejercicio. Despues se hace un set con las notas
                                               #para evitar los repetidos y se busca la posicion de la segunda mas alta, ese valor se lo compara con la lista anidada y se printea.
for x,y in sorted(PythonStudents):             #printea.
    if y==a:
        print(x)
