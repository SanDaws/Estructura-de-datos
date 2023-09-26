from collections import deque 

def array(x):
    return list(map(int, x.split(" ")))
#declaracion de variables
n = array(input())
_revendeLista = deque()
_boletas = n[1]

for i in range(n[0]): 
    _revendeLista.append(array(input()))

i = 1
indice = 0
while _boletas > 0:

    _boletas-= _revendeLista[indice][1]

    if _boletas <= 0:
        print(_revendeLista[indice][0], _boletas + _revendeLista[indice][1])
        break

    if i % 5 == 0:
        _revendeLista.remove(_revendeLista[indice])
        indice-= 1

    if not _revendeLista:
        print("quedaron boletas disponibles")
        break

    i += 1
    indice += 1
    if indice >= len(_revendeLista):
        indice = 0