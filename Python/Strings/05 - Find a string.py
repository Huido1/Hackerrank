#url: https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def count_substring(string, sub_string):
    a = 0
    for i in range (len(string)):
        if sub_string in string[i:i+len(sub_string)]:      #Quiero iterar de 3 en 3, si no agrego ese condicional al string el resultado va a estar mal
            a += 1                                         #entonces al añadir este len del sub string voy a iterar y ver si coincide en funcion de la
    return a                                               #cantidad de letras que tenga. (Leido seria como, si el sub string esta EN string desde la
                                                           #posicion i, hasta la posicion i + len(sub_string)
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
