from collections import deque
 
def calcular_tiempo_espera(N, k, peticiones):
    _tiempo_espera = 0
    fila = deque([(i, p) for i, p in enumerate(peticiones)]) 
 
    while fila:
        ciudadano, peticiones = fila.popleft()
        _tiempo_espera += 5
        peticiones -= 1
 
        if ciudadano == k - 1 and peticiones == 0:
            break 
 
        if peticiones > 0:
            fila.append((ciudadano, peticiones)) 
 
    return _tiempo_espera
 
num_casos = int(input())
 
for _ in range(num_casos):
    N, k = map(int, input().split())
    peticiones = list(map(int, input().split()))
    tiempo_espera = calcular_tiempo_espera(N, k, peticiones)
    print(tiempo_espera)