

def minion_game(string):
    vocales = "AEIOU"
    ke = 0
    st = 0
    
    for i in range(len(string)):             
        if s[i] in vocales:
            ke += len(s) - i
        else:
            st += len(s) - i             #Si inicia con la letra que quiero, el numero de puntos que se sume va a ser la cantidad de letras, menos la posicion.
    if ke > st:                          #ej: En banana, la posicion de a=1 y las letras son 6, entonces va a haber 5 combinaciones que se sumen
        print ("Kevin", ke)
    elif st > ke:
        print ("Stuart", st)
    elif st == ke:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
