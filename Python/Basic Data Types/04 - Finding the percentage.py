#url: https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()                     #Formato del input, va a ser el nombre y una lista de strings con las notas
        scores = list(map(float, line))                   #ahora con un map, ese "line" que era una lista de strings, pasa a ser floats
        student_marks[name] = scores
    query_name = input()                                  #guardas los pares key:value en el diccionario y casteas un nombre
    
    val=0
    for i in student_marks[query_name]:              
        val += i
    res = val / len(student_marks[query_name])            #Entras al diccionario con ese nombre, y cada valor en la lista se suma
                                                          #y se divide por la cantidad de elementos para sacar el promedio
    print('{:.2f}'.format(res))                           #Finalmente, se agrega el comando para formatear el float a 2 decimales.
