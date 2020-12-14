#url: https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))              #Al agregar any, en vez de chequear que se cumpla todo, chequea que se cumpla alguna vez. c es una variable cualquiera.
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
