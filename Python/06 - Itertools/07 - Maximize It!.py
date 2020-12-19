

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

K, M = map(int, input().split())

J = (list(map(int, input().split())) [1:] for i in range(K))         #La idea es que haga una lista, pero sin tomar el primer numero en el input porque no me interesa

res = map(lambda x: sum(i**2 for i in x) % M, itertools.product(*J)) #Se hace lla cuenta que piden, para los productos de la lista unpackeada de antes

print(max(res))
