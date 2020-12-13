#url: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    lista = []
    
    for i in range (N):
        x = input().split(" ")
        command = x[0]                              #Al poner un input con split, el formato va a ser de lista. Por eso, si quiero acceder a la palabra que sera mi command
        if command == "insert":                     #tengo que poner ese x[0] para que coincida y me lo tome. 
            lista.insert(int(x[1]), int(x[2]))
        elif command == "print":
            print(lista)
        elif command == "remove":
            lista.remove(int(x[1]))
        elif command == "append":
            lista.append(int(x[1]))
        elif command == "sort":
            lista.sort()
        elif command == "pop":
            lista.pop()
        elif command == "reverse":
            lista = lista[::-1]
