

def print_rangoli(size):
    letras = "abcdefghijklmnopqrstuvwxyz"          #No agregar la ñ porque algunos casos va a dar error
    data = [letras[i] for i in range(n)]
    items = list(range(n))
    items = items[:-1]+items[::-1]                 #Se crea la secuencia de indices para que se printeen las letras
    for i in items:
        inicio = (i+1)
        original =data[-inicio:]
        invertido = original[::-1]
        fila = invertido+original[1:]              #Con la list comprehension de arriba en funcion de n se crean las letras y luego se usa el join
        fila = "-".join(fila)
        ancho = n*4-3
        fila = fila.center(ancho, "-")
        print(fila)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
