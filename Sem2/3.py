for i in range(int(input())):
    _msj = tuple(input().split())
    _msjJem2 = _msj[::-1]
    _msjJem1 = [""]*len(_msjJem2)
    
    for _cripto in range(0,len(_msjJem1)-1,2):
        _msjJem1[_cripto],_msjJem1[_cripto+1] = _msjJem2[_cripto+1],_msjJem2[_cripto]
        
    if len(_msjJem2)%2!=0:
        _msjJem1.append(_msjJem2[-1])
    print("".join(_msjJem1))