#url: https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys                                                        #Todo esto puesto por defecto en el ejercicio

# Complete the solve function below.
def solve(s):
    return " ".join([i.capitalize() for i in s.split(" ")])       #Basicamente, spliteas el input para que se haga una lista, iteras cada index de la misma aplicando la mayuscula
                                                                  #y pones un join con espacio. Se puede hacer en mas de una linea si se prefiere.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
