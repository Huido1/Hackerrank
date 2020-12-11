#url: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    LiAr = []                           
    
    for i in arr:
        if i not in LiAr:
            LiAr.append(i)
    LiAr.sort(reverse=True)            #Lista vacia, itera cada numero metido en arr y si no esta lo mete en la lista para evitar repetidos (usar set(arr) es lo mismo)
                                       #una vez hecho eso se ordena la lista y se printea. Se puede obviar el reverse y printear asi, es lo mismo.
    print(LiAr[1])
