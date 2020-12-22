#url: https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

n = int(input())
palabra = [input() for i in range(n)]
Counter = collections.Counter(palabra)

print(len(Counter))
print(*Counter.values())
