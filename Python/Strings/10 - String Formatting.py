#url: https://www.hackerrank.com/challenges/python-string-formatting/problem

#Informacion muy util para entender bien la linea 8 y todo lo que sea {}.format(): https://thepythonguru.com/python-string-formatting/

def print_formatted(number):
    m = len("{0:b}".format(number))
    for i in range (1, number+1):
        a = "{i:{m}d} {i:{m}o} {i:{m}X} {i:{m}b}".format(i=i, m=m)
        print (a)
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
