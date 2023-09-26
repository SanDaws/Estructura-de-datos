for i in range(int(input())):
  Y,P = map(int,input().split())

  _arreglo = tuple(map(int, input().split()))
  _prim = True
  for i in range(1, P + 1):
    if P % i == 0 and i not in _arreglo:
        _prim = False
        break

  if _prim:
    print("Es PrimiConjunto")
  else:
    print("No es PrimiConjunto")