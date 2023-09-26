_codigo = ""
_lis = list()
 
while _codigo!="end" : 
    entro= False
    _codigo = input()
 
    if _codigo in "0123456789":
        _lis.append(int(_codigo))
    elif _codigo =="C" and len(_lis)!=0:
        _lis.pop()
    elif "D" in _codigo :
        comando,_Datos = _codigo.split()
        _Datos = int(_Datos)
        if _Datos<=len(_lis):
            for h in range(int(_Datos)):
                _lis.pop()
    elif "M" in _codigo:
        comando,I,J = _codigo.split()
        I = int(I)
        J = int(J)
        while J<=len(_lis) and I<=J:
            entro =True
            print(_lis[I-1],end="")
            I+=1
        if entro:
            print()