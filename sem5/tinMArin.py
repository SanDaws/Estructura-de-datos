"""Bueno, supongamos que el profesor va a repartir al final del curso un regalo sorpresa a un(a) estudiante
 y para ello va a hacer uso de este juego de selección, pero de una manera diferente: Primero se numeran los
 N estudiantes del 1 al N y se organizan formando un circulo. En vez de hacer un conteo "De Tin Marín …" se
 hace un conteo 1, 2, …, K. El estudiante en esa posición sale del circulo y a partir del estudiante a su
 derecha se continúa el procedimiento. Sin embargo, cada vez que sale un estudiante se actualiza el valor
 de K como el módulo entre el número del que acabó de salir y la cantidad de estudiantes restantes. Si ese
 valor da 0 se considera como un 1.

Así por ejemplo, si hay 5 estudiantes y el valor inicial de K es 3, se tendría que:

El primer estudiante en salir es el 3 y el valor de K se actualiza a 3 % 4 = 3

El segundo estudiante en salir es el 1 y el valor de K se actualiza a 1 % 3 = 1

El tercer estudiante en salir es el 2 y el valor de K se actualiza a 2 % 2 = 0, es decir a 1

El cuarto estudiante en salir es el 4, termina el juego, quedando como ganador el 5""" 

for la in range(int(input())):
    _estudiantes, _kontador = map(int, input().split())
    index = 0
    conjunto = [x for x in range(1, _estudiantes+1)]
    while len(conjunto) > 1:
        index = (index + _kontador - 1) % len(conjunto)
        num_eliminado = conjunto.pop(index)
        _kontador = num_eliminado % len(conjunto) if num_eliminado % len(conjunto) != 0 else 1

    print(conjunto[0])   