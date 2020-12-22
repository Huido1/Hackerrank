#url: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

import collections

n = int(input())
dict = collections.OrderedDict()

for i in range(n):
    item = input().rpartition(" ")
    if item[0] not in dict.keys():
        dict[item[0]] = int(item[-1])
    else:
        dict[item[0]] += int(item[-1])
for item in dict:
    print(item, dict[item])
