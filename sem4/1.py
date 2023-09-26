from collections import deque
N = int(input())
 
 
for i in range(N):
    _Apil = deque(input().split())
    _Apil.pop()
    pilaAux = deque()
    estado=0
    for simbolo in _Apil:
        if simbolo in "([{":
            pilaAux.append(simbolo)
            
        elif simbolo in ")]}":
            if not pilaAux:
                print("incorrecta")
                estado = 1
                break
            top = pilaAux.pop()
            
            if (simbolo == ")" and top != "(") or (simbolo == "]" and top != "[") or (simbolo == "}" and top != "{"):
                print("incorrecta")
                break
    if not pilaAux and estado==0:
        print("correcta")
        