#url: https://www.hackerrank.com/challenges/py-if-else/problem

n = int(input())            #No pongas letras porque no te lo toma

if n % 2 == 1:
    print ("Weird")
else:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print ("Weird")
    elif n > 20:             #Cuidado aca, si se usa un "else" tambien va a tomar numeros negativos
        print ("Not Weird")
