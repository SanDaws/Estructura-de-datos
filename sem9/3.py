"""
Bueno, pues resulta que este problema no tiene nada que ver con la película, (excepto por lo de "tri"), 
solo que es muy buena y la recomiendo a quien no la haya visto :P

El problema en realidad es, dado un arreglo A de N números enteros no repetidos, determinar las ternas 
Ai, Aj, Ak con i ≠ j ≠ k que cumplen con Ai + Aj + Ak = T
Input

La entrada comienza con una línea que contiene dos valores enteros positivos separados entre sí por 
un espacio en blanco: el valor de N (3 ≤ N ≤ 1000) y el valor de T. Luego siguen N líneas con los 
elementos del arreglo, cada uno no mayor a 100.000
Output

La salida debe mostrar, de a una por línea, separados entre sí por un espacio en blanco, y en orden 
ascendente según Ai, luego Aj, luego Ak, las ternas que cumplen con la condición. No habrá más de 
100.000 ternas que cumplan y, en caso de no haber ninguna, se deberá mostrar el mensaje (sin comillas): 
'No hay trillizas'.
"""
datos=set()
cantidad_Suma=int(input().split())
for i in range(cantidad_Suma[0]):
    datos.add(input())
if (a+b==cantidad_Suma[1]-c)in datos:
    
