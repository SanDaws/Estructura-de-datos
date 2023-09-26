diferencia = tuple()

for i in range(int(input())):
    _Money = tuple(map(int, input().split()))
    M = _Money[0]
    N = _Money[1]
    _plata = tuple(map(int, input().split()))
    _dinPersona = [0]*M 
    _posi = 0
    for plata in _plata:
        _dinPersona[_posi] += plata
        _posi+=1
        _posi = _posi%M 
    diferencia += (max(_dinPersona) - min(_dinPersona),)
    
for dif in diferencia:
    print(dif)