"""
SUPONGAMOS, que el profesor de un curso, digamos estructuras de datos, va a dar un premio al 
finalizar el curso. ¿En qué consiste? Bueno, SUPONGAMOS que va a repartir una determinada cifra, 
SUPONGAMOS un millón de rials (moneda de Irán), de manera equitativa entre aquellos(as) estudiantes 
que hayan resuelto los 5 ejercicios más difíciles del curso. Tu tarea, si decides aceptarla, es determinar 
qué cantidad de rials (redondeado al entero por debajo) le corresponde a cada estudiante ganador.
Input

La entrada comienza con una línea que contiene la cantidad N1 (0 < N1 < 5000) de estudiantes que resolvieron 
el ejercicio 1. Luego siguen N1 líneas, cada una con la identificación del(la) estudiante que resolvió el 
ejercicio 1. Las identificaciones son valores enteros positivos menores a diez mil millones. Luego sigue una 
línea que contiene la cantidad N2 (0 < N2 < 5000) de estudiantes que resolvieron el ejercicio 2. Luego siguen 
N2 líneas, cada una con la identificación del(la) estudiante que resolvió el ejercicio 2. Y así sucesivamente para los otros 3 ejercicios.
Output

La salida debe mostrar en una única el premio que recibe cada estudiante merecedor del mismo, o el mensaje 
(sin comillas) "Nadie gana" en caso que no haya ninguno. 
"""
"""
3
1000001
1000002
1000003
4
1000002
1000004
1000001
1000003
2
1000001
1000003
2
1000003
1000001
5
1000005
1000001
1000004
1000002
1000003
"""
w1,w2,w3,w4,w5=set(),set(),set(),set(),set()
listDeSet=[w1,w2,w3,w4,w5]
for i in listDeSet:
    for h in range(int(input())):
        i.add(input())

for j in listDeSet:
    w1.intersection_update(j)

if len(w1)==0:print("Nadie gana")
else:print(1000000//(len(w1)))

    
