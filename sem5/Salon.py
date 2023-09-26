"""Hay N jugadores. Uno por uno, deben entrar a una habitación de la que desconocen cuántos
 jugadores hay dentro. Antes de entrar deben escoger un número entero positivo. Al entrar, 
 si el número k que escogieron ya corresponde al de alguno de los jugadores dentro de la 
 habitación, ambos quedan eliminados. Si lo anterior no ocurre, pero alguno de los 
 jugadores dentro de la habitación tiene un valor de k+1, ambos quedan eliminados. Si lo 
 anterior tampoco ocurre, pero alguno de los jugadores dentro de la habitación tiene un 
 valor de k-1, ambos quedan eliminados. Al final del juego se reparte un premio en efectivo 
 entre los jugadores "sobrevivientes"."""

_habitacion=list()

while True:
    _numero= int(input())
    if _numero==0:break
    _numMay=_numero+1
    _numMen=_numero-1
    if not _numero in _habitacion:_habitacion.append(_numero)
    for i in _habitacion:
        if i == _numMay and _numMay in _habitacion: _habitacion.remove(i)
        if i== _numMen and _numMen in _habitacion: _habitacion.remove(i)
    if _numMay in _habitacion:_habitacion.remove(_numMay)
    
if len(_habitacion)==0:print("0")
else:
    txt= ' '.join(map(str,_habitacion))
    print(txt)