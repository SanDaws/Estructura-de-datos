
C=int(input())
_suma=0
_lista= tuple(map(int,input().split()))
for i in reversed(_lista):
    _listasumatoria=tuple(map(_suma+i,_lista))
for i in _listasumatoria:
    if i==_listasumatoria[0]: continue
    else: print(i)

